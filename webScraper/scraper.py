import pandas as pd
import os
from urllib.parse import urlencode
import requests
from datetime import date
from datetime import datetime
import time
import csv
import json
from webScraper.models import Collection_Year, Contact_Details, Business, Local_Government, Classification

# A SAFE GUARD TO PREVENT INIFINITE CALLS TO API
API_LIMIT = 5
API_KEY = os.environ["PLACES_API"]

# Option to save responses from google api
SAVE_API_DATA = False

# TODO: Read in json file of headers instead of hard coding it?
HEADERS = [
    "local_government_area",
    "business_id",
    "places_id",
    "collection_year",
    "business_name",
    "temp_business_types",
    "classification_name",
    "category_1",
    "sub_category_1",
    "category_2",
    "sub_category_2",
    "category_3",
    "sub_category_3",
    "y_latitude",
    "x_longitude",
    "original_lga_provided_address",
    "formatted_address",
    "contact_1",
    "contact_2",
    "email",
    "website",
    "menu_(yes,_provided_on_website/no)",
    "children's_menu_provided_(yes/no)",
    "opening_hours",
    "notes",
]


def get_lga_list():
    shire_list = []

    with open("./map/geoJSON/metro_area_lga.txt", "r") as f:
        for line in f:
            shire_list.append(line.strip())

    shire_list


# NOT USED
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


#-----------------------CALLS TO API--------------------------------------------------------------


def request_contact_info(place_id: str, api_key: str) -> dict:
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
        "key" : api_key,
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

def request_basic_info(name: str, addr: str, api_key: str) -> dict:
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
        "key" : api_key,
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


def req_place_details(df: pd.DataFrame, api_key: str) -> tuple:
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
    basic_details = request_basic_info(name, addr, api_key)

    status = get_status(basic_details)

    if status == "OK":
        # Extract the place id, we will need it to request
        # contact details
        place_id = extract_places_id(basic_details)

        # Call google api for contact info
        contact_details = request_contact_info(place_id, api_key)

        return (basic_details, contact_details)
    else:
        return None


#----------------------------HELPERS-----------------------------------
# These are some functions to extract details from the 
# basic details and contact detail objects
def get_formatted_addr(basic: tuple) -> str:
    '''
    Extracts formatted address from Google Places API json response

    Param:
        basic: tuple containing basic data json and contact details json

    Return:
        str: Formatted address of the business
    '''

    if "formatted_address" in basic[0]["candidates"][0]:
        return basic[0]["candidates"][0]["formatted_address"]
    else:
        return "-"

def get_lat_long(basic: tuple) -> tuple:
    '''
    Extracts long and lat from Google Places API json response

    Param:
        basic: tuple containing basic data json and contact details json

    Return:
        tuple: int representation of lat and long
    '''
    lat = str(basic[0]["candidates"][0]["geometry"]["location"]["lat"])
    lng = str(basic[0]["candidates"][0]["geometry"]["location"]["lng"])
    return (lat, lng)


def get_business_types(basic: tuple) -> list:
    '''
    Extracts a list of types the business falls under

    Param:
        basic: tuple containing basic data json and contact details json

    Return:
        list: decirptive words of the business
    '''

    if "types" in basic[0]["candidates"][0]:
        return basic[0]["candidates"][0]["types"]
    else:
        return "-"

# TODO: return a int instead?
def get_phone_no(basic: tuple) -> str:
    '''
    Extracts the phone number

    Param:
        basic: tuple containing basic data json and contact details json

    Return:
        str: phone number
    '''
    
    if "formatted_phone_number" in basic[1]["result"]:
        return basic[1]["result"]["formatted_phone_number"]
    else:
        return "-"


# TODO: add defensive programming clauses, i.e. what if invalid given for format
def get_opening(basic: tuple, format="periods") -> dict:
    '''
    Extracts the opening hours

    Param:
        basic: tuple containing basic data json and contact details json

    format: 
        default is "periods" will return a dictionary representation of the opening and closing hours
        "text" will return an easy to read text representation of opening and closing hours

    Return:
        json: opening hours
    '''

    if "opening_hours" in basic[1]["result"]:

        if format == "periods":
            
            return basic[1]["result"]["opening_hours"]["periods"]

        elif format == "text":

            return basic[1]["result"]["opening_hours"]["weekday_text"]

    return "-"


def get_website(basic: tuple) -> str:
    '''
    Extracts the website
        
    Param:
        basic: tuple containing basic data json and contact details json

    Return:
        str: The website or an empty string if no website exists
    '''
    # Business has a website return the website else send an emtpy string
    if "website" in basic[1]["result"]:
        return basic[1]["result"]["website"]
    else:
        return "-"


def extract_places_id(basic: dict):

    return basic['candidates'][0]['place_id']


def get_status(basic: dict):
    return basic["status"]

#---------------------------------------------------------------------------------------
# The following functions take in a list and place data in the correct index

def fill_empty(length: int, fill="") -> list:
    return [fill for x in range(length)]


def add_name(lst: list, headers: list, df: pd.DataFrame) -> None:
    index = headers.index("business_name")
    lst[index] = df.loc["business_name"]


def add_lga(lst: list, headers: list, lga: str) -> None:
    index = headers.index("local_government_area")
    lst[index] = lga


def add_year(lst: list, headers: list) -> None:
    year = date.today().year
    index = headers.index("collection_year")
    lst[index] = year


def add_lat_long(lst: list, headers: list, data: tuple) -> None:
    coordinates = get_lat_long(data)
    lat_index = headers.index("y_latitude")
    long_index = headers.index("x_longitude")

    lst[lat_index] = coordinates[0]
    lst[long_index] = coordinates[1]


def add_phone(lst: list, headers: list, data: tuple) -> None:
    phone_no = get_phone_no(data)
    index = headers.index("contact_1")
    lst[index] = phone_no


def add_website(lst: list, headers: list, data: tuple) -> None:
    website = get_website(data)
    index = headers.index("website")
    lst[index] = website


# TODO: add conditions on shop address that are inside a shopping centre
def add_address(lst: list, headers: list, data: dict, curr: pd.DataFrame) -> None:
    address = get_formatted_addr(data).split()
    address = [x.replace(",", "") for x in address]
    orig_addr = curr.loc["parcel_address"]

    num_index = headers.index("new_street_number")
    name_index = headers.index("new_street_name")
    type_index = headers.index("new_street_type")
    suffix_index = headers.index("new_street_suffix") # NOT USED
    suburb_index = headers.index("new_suburb")
    postcode_index = headers.index("new_postcode")
    orig_index = headers.index("original_lga_provided_address")

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
    

def add_formatted_address(lst: list, headers: list, data: dict, curr: pd.DataFrame) -> None:
    orig_addr = curr.loc["parcel_address"]
    format_addr_index = headers.index("formatted_address")
    orig_index = headers.index("original_lga_provided_address")

    lst[orig_index] = orig_addr
    lst[format_addr_index] = get_formatted_addr(data)


# TODO: add the sums of the weekends and weekdays
def add_opening_times(lst: list, headers: list, data: dict) -> None:
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

        open_index = headers.index(current_day+"open")
        close_index = headers.index(current_day+"close")
        hrs_index = headers.index(current_day+"total_hrs")

        lst[open_index] = o_time
        lst[close_index] = c_time
        lst[hrs_index] = total_hrs

    for closed, day in enumerate(is_open):
        if closed:
            current_day = days_index[day]
            open_index = headers.index(current_day+"open")
            close_index = headers.index(current_day+"close")
            hrs_index = headers.index(current_day+"total_hrs")

            lst[open_index] = "closed"
            lst[close_index] = "closed"
            lst[hrs_index] = "closed"


def add_places_id(lst: list, headers: list, data: dict) -> None:
    places_id = extract_places_id(data[0])
    id_index = headers.index("places_id")

    lst[id_index] = places_id


def add_types(lst: list, headers: list, data: dict) -> None:
    b_types = get_business_types(data)
    types_index = headers.index("temp_business_types")
    b_types_to_str = ", ".join(b_types)
    lst[types_index] = b_types_to_str

#TODO: currently the unicode "\u2013" which is a "-" does not get printed properly
#       we need to replace it with something else or the correct unicode for "-"
def add_json_opening_hours(lst: list, headers: list, data: dict) -> None:
    opening_index = headers.index("opening_hours")
    opening = get_opening(data, format="text")

    lst[opening_index] = json.dumps(opening, separators=(",", ":"))



def write_to_csv(data: pd.DataFrame, filename: str) -> None:
    dir_loc = f'./test_files/outputs/{filename}'
    with open(dir_loc, "w") as f:
        write = csv.writer(f)
        write.writerows(data)


def dump_json_data(curr: pd.DataFrame, data: dict) -> None:
    format_name = curr.loc["business_name"].title().replace(" ", "")
    location = f"./test_files/api_business_data/{format_name}.json"

    with open(location, "w") as output:
        json.dump([data[0], data[1]], output)

#---------------------------MAIN------------------------------------


def get_cleaned_table(file: str, lga: str, api_key: str) -> list:
    # Elapsed time start
    start = time.perf_counter()

    # scraped list
    cleaned_data = list()
    df = read_file(file)
    cleaned_data.append(HEADERS)

    # list of businesses places could not find data
    no_online_data = list()
    no_online_data.append(HEADERS)

    num_business = df.shape[0]
    num_headers = len(HEADERS)

    num_calls = 0
    print("Scraping....")
    for i in range(num_business):
        if num_calls == API_LIMIT:
            break

        # Create a list with x empty elements
        new_row = fill_empty(num_headers)
        curr_business = df.iloc[i, :]

        print(f"{curr_business.loc['business_name']}...")

        # Scraped data will be None if Google cannot find anything
        scraped_data = req_place_details(curr_business, api_key)

        if not scraped_data == None:

            # For testing, this will print out the response data and break
            if SAVE_API_DATA:
                dump_json_data(curr_business, scraped_data)
                break

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
            #add_address(new_row, HEADERS, scraped_data, curr_business)
            # Filles the opening times fields
            #add_opening_times(new_row, HEADERS, scraped_data)

            add_types(new_row, HEADERS, scraped_data)
            add_places_id(new_row, HEADERS, scraped_data)
            add_json_opening_hours(new_row, HEADERS, scraped_data)
            add_formatted_address(new_row, HEADERS, scraped_data, curr_business)

            cleaned_data.append(new_row)

        else:
            # Fills the lga name field
            add_lga(new_row, HEADERS, lga)
            # Fills the collection year field
            add_year(new_row, HEADERS)
            # Fills the name of the business field
            add_name(new_row, HEADERS, curr_business)

            no_online_data.append(new_row)



        #TODO add classification
        #TODO add Categories

        #TODO add email

        #TODO add menu
        #TODO add childrens menu

        # Add the row to the cleaned data list
        

        num_calls += 1

    # Elapsed time end
    end = time.perf_counter()
    print("Finised in {:.3g} seconds".format(end-start))

    return (cleaned_data, no_online_data)

