import pandas as pd
import numpy as np
import os
from urllib.parse import urlencode
import requests
from datetime import date
from datetime import datetime
import time
import csv


# A SAFE GUARD TO PREVENT INIFINITE CALLS TO API
API_LIMIT = 5

API_KEY = os.environ["PLACES_API"]

# TODO: Read in json file of headers instead of hard coding it?
HEADERS = {
    "local_government_area":    0,
    "redcap_id":                1,
    "business_id":              2,
    "collection_year":          3,
    "business_name":            4,
    "classification_name":      5,
    "category_1":               6,
    "sub_category_1":           7,
    "category_2":               8,
    "sub_category_2":           9,
    "category_3":               10,
    "sub_category_3":           11,
    "y_latitude":               12,
    "x_longitude":              13,
    "original_lga_provided_address": 14,
    "new_unit_shop_number":     15,
    "new_street_number":        16,
    "new_street_name":          17,
    "new_street_type":          18,
    "new_street_suffix":        19,
    "new_suburb":               20,
    "new_postcode":             21,
    "contact_1":                22,
    "contact_2":                23,
    "email":                    24,
    "website":                  25,
    "menu_(yes,_provided_on_website/no)": 26,
    "children's_menu_provided_(yes/no)": 27,
    "mon_open":                 28,
    "mon_close":                29,
    "mon_total_hrs":            30,
    "tues_open":                31,
    "tues_close":               32,
    "tues_total_hrs":           33,
    "weds_open":                34,
    "weds_close":                35,
    "weds_total_hrs":            36,
    "thurs_open":               37,
    "thurs_close":               38,
    "thurs_total_hrs":           39,
    "fri_open":                 40,
    "fri_close":                41,
    "fri_total_hrs":            42,
    "sat_open":                 43,
    "sat_close":                44,
    "sat_total_hrs":            45,
    "sun_open":                 46,
    "sun_close":                47,
    "sun_total_hrs":            48,
    "total_weekdays_hrs":       49,
    "total_weekend_hrs":        50,
    "notes":                    51
}

def get_business_name_add(file: str) -> dict:
    '''
    Extracts business name and address from a pandas DataFrame

    Params:
        file: str representation of the file path

    Return:
        Dictionary: key(str) = name of business
                    value(str) = address of business
    '''
    df = read_file(file)
    name_addr = dict()

    # Get the rows x column in tuple form
    shape = df.shape

    rows = shape[0]

    for i in range(rows):
        line = df.iloc[i, :]
        business_name = line["business_name"]
        addr = line["parcel_address"]
        name_addr[business_name] = addr

    return name_addr


def read_file(file: str) -> pd.DataFrame:
    '''
    Reads a xls or xlsx file
    Params:
        file: str representation of the file path

    Return:
        Pandas DataFrame
    '''
    # Read in the file
    data = pd.read_excel(file)

    # Drop all empty Rows
    data = data.dropna(how="all")

    # Replace nan with an empty string
    data = data.fillna("")

    # If we dont have headers. We allocate it.
    if True in data.columns.str.contains("^Unnamed"):
        # Define the headers
        data.columns = data.iloc[0]
        # Reset the index
        data.iloc[1:].reset_index(drop=True)
        # skip the first row, which is a copy of our column reference.
        data = data[1:]

    # Clean headers, strip leading and trailing spaces. convert lowercase and replace spaces seperating words with a underscore 
    data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_")

    return data


def request_contact_info(place_id: str) -> dict:
    '''
    Calls Google Places API for contact information. phone number, opening hours, and website

    Params:
        name: string of the business name
        addr: string of the business address

    Return:
        Dictionary containing contact details
    '''
    format = 'json'
    base_endpoints_place = f'https://maps.googleapis.com/maps/api/place/details/{format}'
    params = {
        "key" : API_KEY,
        "place_id" : place_id,
        "fields" : "formatted_phone_number,opening_hours,website"
    }

    params_encoded = urlencode(params)

    places_endpoint = f'{base_endpoints_place}?{params_encoded}'
    
    # send the request
    r = requests.get(places_endpoint)

    if r.status_code != 200:
        print(f"Error retrieving contact details: with error code {r.status_code}")
        return {}

    return r.json()

def request_basic_info(name: str, addr: str) -> dict:
    '''
    Calls Google Places API for formatted address, geometry(lattitude, longitude), name of the business,
    place identifier, and business type

    Params:
        name: string of the business name
        addr: string of the business address

    Return:
        Dictionary containing place details
    '''

    # This is used as a radius of our search
    perth =[-31.95256861099548, 115.86077042146033]
    # The file format we want back from the api
    format = 'json'
    # end points of the api
    base_endpoints_place = f'https://maps.googleapis.com/maps/api/place/findplacefromtext/{format}'

    search_str = f"{name} {addr}"

    params = {
        "key" : API_KEY,
        "input" : search_str,
        "inputtype": "textquery",
        "fields" : "formatted_address,geometry,name,place_id,type"
    }

    location_bias = f'point:{perth[0]},{perth[1]}'

    # Adds radius to search
    use_circular = True
    if use_circular:
        radius = 60000
        location_bias = f'point:{radius}@{perth[0]},{perth[1]}'


    params['locationbias'] = location_bias
    params_encoded = urlencode(params)
    places_endpoint = f'{base_endpoints_place}?{params_encoded}'

    # send the request
    r = requests.get(places_endpoint)

    if r.status_code != 200:
        print(f"Error retrieving basic data: with error code {r.status_code}")
        return {}

    return r.json()


def req_place_details(df: pd.DataFrame) -> tuple:
    '''
    Helper function requests both business details and contact information

    Param:
        df: DataFrame containing business name and parcel address

    Return:
        Tuple: dictionary of the details and a dictionary of the contact information.
    '''

    name = df.loc["business_name"]
    addr = df.loc["parcel_address"]

    # call google api for buiness info
    basic_details = request_basic_info(name, addr)

    # Extract the place id, we will need it to request
    # contact details
    place_id = basic_details['candidates'][0]['place_id']

    # Call google api for contact info
    contact_details = request_contact_info(place_id)

    return (basic_details, contact_details)


#----------------------------HELPERS-----------------------------------
# These are some functions to extract details from the 
# basic details and contact detail objects
def get_formatted_addr(basic):
    return basic[0]["candidates"][0]["formatted_address"]


def get_lat_long(basic):
    lat = basic[0]["candidates"][0]["geometry"]["location"]["lat"]
    lng = basic[0]["candidates"][0]["geometry"]["location"]["lng"]
    return (lat, lng)


def get_business_types(basic):
    return basic[0]["candidates"][0]["types"]


def get_phone_no(contact):
    return contact[1]["result"]["formatted_phone_number"]


def get_opening(contact, format="periods"):
    if format == "periods":
        return contact[1]["result"]["opening_hours"]["periods"]
    else:
        return contact[1]["result"]["opening_hours"]["weekday_text"]


def get_website(contact):

    # Business has a website return the website else send an emtpy string
    if "website" in contact[1]["result"]:
        return contact[1]["result"]["website"]
    else:
        return " "


#---------------------------------------------------------------------------------------
# The following functions take in a list and place data in the correct index

def fill_empty(length, fill=""):
    return [fill for x in range(length)]


def add_name(lst: list, headers: dict, df: pd.DataFrame):
    index = headers["business_name"]
    lst[index] = df.loc["business_name"]


def add_lga(lst: list, headers: dict, lga: str):
    index = headers["local_government_area"]
    lst[index] = lga


def add_year(lst: list, headers: dict):
    year = date.today().year
    index = headers["collection_year"]
    lst[index] = year


def add_lat_long(lst: list, headers: dict, data: tuple):
    coordinates = get_lat_long(data)
    lat_index = headers["y_latitude"]
    long_index = headers["x_longitude"]
    lst[lat_index] = coordinates[0]
    lst[long_index] = coordinates[1]


def add_phone(lst: list, headers: dict, data: tuple):
    phone_no = get_phone_no(data)
    index = headers["contact_1"]
    lst[index] = phone_no


def add_website(lst: list, headers: dict, data: tuple):
    website = get_website(data)
    index = headers["website"]
    lst[index] = website


# TODO: add conditions on shop address that are inside a shopping centre
def add_address(lst: list, headers: dict, data: dict, curr: pd.DataFrame):
    address = get_formatted_addr(data).split()
    address = [x.replace(",", "") for x in address]
    orig_addr = curr.loc["parcel_address"]

    num_index = headers["new_street_number"]
    name_index = headers["new_street_name"]
    type_index = headers["new_street_type"]
    suffix_index = headers["new_street_suffix"] # NOT USED
    suburb_index = headers["new_suburb"]
    postcode_index = headers["new_postcode"]
    orig_index = headers["original_lga_provided_address"]

    # Street Number
    lst[num_index] = address[0]
    # Street name
    lst[name_index] = address[1]
    # Street Type
    lst[type_index] = address[2]
    # Suburb
    lst[suburb_index] = address[3]
    # Postcode
    lst[postcode_index] = address[5]
    # Original lga provided address
    lst[orig_index] = orig_addr
    

# TODO: add the sums of the weekends and weekdays
def add_opening_times(lst: list, headers: dict, data: dict):
    FMT = '%H%M'
    DAYS = 7

    days_index = {
        0: "sun_",
        1: "mon_",
        2: "tues_",
        3: "weds_",
        4: "thurs_",
        5: "fri_",
        6: "sat_"
    }

    is_open = [False for x in range(DAYS)]
    opening = get_opening(data)

    for period in opening:
        total_hrs = 0
        day = period["close"]["day"]
        current_day = days_index[day]
        is_open[day] = True

        o_time = -1
        c_time = period["close"]["time"]

        if period["open"]["day"] == day:
            o_time = period["open"]["time"]
        else:
            print("Days do not match")
            break
        
        total_hrs = datetime.strptime(c_time, FMT) - datetime.strptime(o_time, FMT)
        total_hrs = total_hrs.total_seconds() / 60 / 60

        open_index = headers[current_day+"open"]
        close_index = headers[current_day+"close"]
        hrs_index = headers[current_day+"total_hrs"]

        lst[open_index] = o_time
        lst[close_index] = c_time
        lst[hrs_index] = total_hrs

    for closed, day in enumerate(is_open):
        if closed:
            current_day = days_index[day]
            open_index = headers[current_day+"open"]
            close_index = headers[current_day+"close"]
            hrs_index = headers[current_day+"total_hrs"]

            lst[open_index] = "closed"
            lst[close_index] = "closed"
            lst[hrs_index] = "closed"


def write_to_csv(data, filename):
    with open(filename, "w") as f:
        write = csv.writer(f)
        write.writerows(data)


#---------------------------MAIN------------------------------------


def main(file: str, lga: str):
    # Elapsed time start
    start = time.time()

    cleaned_data = list()
    df = read_file(file)
    cleaned_data.append(list(HEADERS.keys()))

    num_business = df.shape[0]
    num_headers = len(list(HEADERS.keys()))

    num_calls = 0
    for i in range(num_business):

        if num_calls == API_LIMIT:
            break

        # Create a list with x empty elements
        new_row = fill_empty(num_headers)
        curr_business = df.iloc[i, :]
        scraped_data = req_place_details(curr_business)

        # Fills the lga name field
        add_lga(new_row, HEADERS, lga)
        # Fills the collection year field
        add_year(new_row, HEADERS)
        # Fills the name of the business field
        add_name(new_row, HEADERS, curr_business)
        # Fills latitude and longitude field
        add_lat_long(new_row, HEADERS, scraped_data)
        # Fills phone number field
        add_phone(new_row, HEADERS, scraped_data)
        # Fills website field
        add_website(new_row, HEADERS, scraped_data)
        # Fills address fields
        add_address(new_row, HEADERS, scraped_data, curr_business)
        # Filles the opening times fields
        add_opening_times(new_row, HEADERS, scraped_data)


        #TODO add classification
        #TODO add Categories

        #TODO add email

        #TODO add menu
        #TODO add childrens menu

        # Add the row to the cleaned data list
        cleaned_data.append(new_row)

        num_calls += 1

    # Elapsed time end
    end = time.time()
    print("Finised in {:.3g} seconds".format(end-start))

    return cleaned_data



DATA_FILE = "test_files/Food Business Listing 2021.22 - CoA Summary.xls"
CAKEAWAY = "./test_files/CakeawaybySina.xlsx"
CHANDAS = "./test_files/Chanda'sFamilyChildCare.xlsx"
JINGS = "./test_files/Jing's Noodle Bar Kelmscott.xls"
SANDC = "./test_files/S and C Fiolo.xls"
LGA = "Armadale, City of"

sample_cleaned_csv = main(JINGS, LGA)

write_to_csv(sample_cleaned_csv, "JINGS_SAMPLE.csv")


# print(main(CAKEAWAY))
# print(main(CHANDAS))
# print(main(JINGS))
# print(main(SANDC))
#get_business_name_add(DATA_FILE)

# df = read_file(DATA_FILE)

# print(type(df.keys()))

# print(isinstance(df, pd.DataFrame))

