from webScraper.models import Collection_Year, Contact_Details, Business, Local_Government, Classification
from webScraper.scraper import *


def add_local_gov(coll_year: int):
    gov_file = "map/geoJSON/metro_area_lga.txt"

    gov_list = []

    with open(gov_file, "r") as f:

        for line in f:
            gov_list.append(line.strip())

    
    year_obj = Collection_Year.objects.filter(year=coll_year)

    if len(year_obj) == 0:
        year_obj = Collection_Year.objects.create(year=coll_year)
        year_obj.save()
        print("New Collection Created")
    else:
        year_obj = year_obj[0]

    for lga in gov_list:
        new_lga_obj = Local_Government.objects.filter(local_government_area=lga, year=year_obj)
        if len(new_lga_obj) == 0:
            new_lga_obj = Local_Government.objects.create(local_government_area=lga, year=year_obj)
        else:
            new_lga_obj = new_lga_obj[0]


def add_excel_to_db(file: str):
    #fremantle = "webScraper/test_files/fremantle_cleaned.xlsx"

    data = read_file(file)

    num_business = data.shape[0]
    num_headers = len(HEADERS)

    num_calls = 0
    print("Adding to db...")
    for i in range(num_business):
        # Create a list with x empty elements
        curr_business = data.iloc[i, :]
        name = curr_business.loc['business_name']
        print(f"{name}...")

        lga = curr_business.loc['local_government_area'].upper()

        coll_year = int(curr_business.loc['collection_year'])
        classification = curr_business.loc['classification']
        cat_one = curr_business.loc['category_1']
        parcel_address = curr_business.loc['original_lga_provided_address']
        formatted_add = curr_business.loc['formatted_address']
        phone = curr_business.loc['contact_1']
        web = curr_business.loc['website']
        places_id = curr_business.loc['places_id']
        y_latitude = float(curr_business['y_latitude'])
        x_longitude = float(curr_business['x_longitude'])

        year_obj = Collection_Year.objects.filter(year=coll_year)[0]
        db_lga = Local_Government.objects.filter(local_government_area=lga, year=year_obj)[0]

        db_business = Business.objects.create(local_government_area=db_lga, business_name=name, google_id=places_id)
        db_business.save()
        db_classification = Classification.objects.create(business_id=db_business)
        db_classification.possible_classifications = classification
        db_classification.possible_categories = cat_one
        db_classification.save()
        db_contact = Contact_Details.objects.create(business_id=db_business, 
                                                    parcel_address=parcel_address, 
                                                    formatted_address=formatted_add,
                                                    phone=phone,
                                                    website=web,
                                                    longitude=x_longitude,
                                                    latitude=y_latitude)
        db_contact.save()
    return

def add_minimal_excel_to_db(file: str):

    test_one = "webScraper_script/test_files/2022_files/ALL FOOD BUSINESS DATA 2022.xlsx"
    data = read_file(test_one)

    num_business = data.shape[0]
    num_headers = len(HEADERS)

    num_calls = 0
    print("Adding to db...")
    for i in range(num_business):
        # Create a list with x empty elements
        curr_business = data.iloc[i, :]
        name = str(curr_business.loc['business_name']).strip()
        lga = curr_business.loc['local_government_area'].upper().strip()

        if lga == "COCKBURN, CITY OF":
            print(f"{name}...")
            coll_year = int(curr_business.loc['collection_year'])
            classification = curr_business.loc['classification']
            cat_one = curr_business.loc['category_1']
            # parcel_address = name.split("-", 1)

            # if len(parcel_address) == 2:
            #     name = parcel_address[0].strip()
            #     parcel_address = parcel_address[1].strip()

            parcel_address = curr_business.loc['original_lga_provided_address'].strip()
            phone = curr_business.loc['contact_number_1']
            web = curr_business.loc['website']

            y_latitude = curr_business['y_latitude']
            x_longitude = curr_business['x_longitude']

            if len(y_latitude) > 0:
                y_latitude = float(y_latitude)
                x_longitude = float(x_longitude)
            else:
                y_latitude = -31.9524993
                x_longitude = 115.8612164

            year_obj = Collection_Year.objects.filter(year=coll_year)[0]
            db_lga = Local_Government.objects.filter(local_government_area=lga, year=year_obj)[0]

            db_business = Business.objects.create(local_government_area=db_lga, business_name=name)
            db_business.save()
            db_classification = Classification.objects.create(business_id=db_business)
            db_classification.possible_classifications = classification
            db_classification.possible_categories = cat_one
            db_classification.save()
            db_contact = Contact_Details.objects.create(business_id=db_business, 
                                                        parcel_address=parcel_address,
                                                        phone=phone,
                                                        website=web,
                                                        longitude=x_longitude,
                                                        latitude=y_latitude)
            db_contact.save()
    return