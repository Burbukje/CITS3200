# Food Atlas - Scraper Module


## [Processing inputs](#processing-inputs-1)
- [Headers](#headers)
- [Processing xls and slsx input files](#routines)

## [API Requests](#api-requests-1)
- [Requesting both basic information and contact details](#routines-1)
- [Basic Information](#routines-1)
- [Contact Details](#routines-1)

## [Extracting Data from API response](#extracting-data-from-api-response-1)
- [Formatted Address](#routines-2)
- [Lattitudes and Longitudes](#routines-2)
- [Business Type](#routines-2)
- [Phone Number](#routines-2)
- [Opening Hours](#routines-2)
- [Website](#routines-2)


## [Creating a data files](#creating-data-files)
- [Writing to csv file]()
- [Writing Google Responses to file]()

#

# Processing Inputs
This scraper program can process excel files, extracting data required for Google Places API calls.

## Headers
Headers must fit the specifications detailed in the headers_format.md documentation.

## **Routines**
#


`read_file(file)`
- Reads in a excel file and returns a pandas Dataframe

**Parameters:**
- **file:** *string*
    - directory to the file

#

# API Requests
In this module we will be using Googles Places Api to request information on a business.

Data requested includes:

Basic Information:
- Google Place's unique 'Place ID'
- Formated Address
- Location (longitude and latitude)
- Business Name
- Business Type

Contact Information:
- Phone Number
- Opening Hours
- Website

## **Routines**
# 

`req_place_details(df, api_key)`
- This function will call both `request_contact_info(df, api_key)` and `request_basic_info(df, api_key)` for ease of use and return a tuple. 
    1. A dictionary object containing the basic information 
    2. And a dictionary object containing the contact information

**Parameters:**
- **df:** *pandas.DataFrame*
    - the DataFrame returned from calling `read_file(file)`
- **api_key:** *str*
    - your api key for google places
#

`request_contact_info(df, api_key)`
- Will send a request to Google Places API and return a dictionary containing the contact information

**Parameters:**
- **df:** *pandas.DataFrame*
    - the DataFrame returned from calling `read_file(file)`
- **api_key:** *str*
    - your api key for google places
#

`request_basic_info(df, api_key)`
- Will send a request to Google Places API and return a dictionary object containing the basic information 

**Parameters:**
- **df:** *pandas.DataFrame*
    - the DataFrame returned from calling `read_file(file)`
- **api_key:** *str*
    - your api key for google places
#


# Extracting Data from API response
This module contains mainly helpers and the only function you need to call will be `get_cleaned_table(file, lga, api_key)` as this function will loop through all businesses and call each helper

## Routines
#
`get_cleaned_table(file, lga, api_key)`
- Return a list containing cleaned data for all businesses

**Parameters:**
- **file:** *str*
    - directory to the excel file
- **lga:* *str*
    - The local government name for the current data
- **api_key:** *str*
    - your api key for google places

#

## Helpers

#
`get_formatted_addr(basic)`

- Return formatted address from Google Places API json response

**Parameters:**
- **basic:** *tuple*
    - A tuple return by `req_place_details(df, api_key)`
#

`get_lat_long(basic)`
- Returns long and lat from Google Places API json response

**Parameters:**
- **basic:** *tuple*
    - A tuple return by `req_place_details(df, api_key)`
#

`get_business_types(basic)`
- Returns a list of types the business falls under

**Parameters:**
- **basic:** *tuple*
    - A tuple return by `req_place_details(df, api_key)`
#

`get_phone_no(basic)`
- Returns the phone number

**Parameters:**
- **basic:** *tuple*
    - A tuple return by `req_place_details(df, api_key)`
#

`get_opening(basic, format="periods")`
- Returns the opening hours

**Parameters:**
- **basic:** *tuple*
    - A tuple return by `req_place_details(df, api_key)`
- **format:** *str, optional*
    - format of the opening hours default is "periods"
    - format="text" will return a human readable text

#

`def get_website(basic: tuple)`
- Returns the website or an empty string if website does not exist.

**Parameters:**
- **basic:** *tuple*
    - A tuple return by `req_place_details(df, api_key)`

#

# Creating Data Files
We can write the cleaned data return by `get_cleaned_table(file, lga, api_key)` using `write_to_csv(data, filename)` and responses return by `req_place_details(df, api_key)` using `dump_json_data(curr, data)`

## Routines
#
`write_to_csv(data, filename)`

**Parameters:**
- **data:** *list*
    - A list return by `get_cleaned_table(file, lga, api_key)`

- **filename:** *list*
    - files will be saved in the apporiate folder in the "test_files" folder

#

`dump_json_data(curr, data)`

**Parameters:**
- **data:** *tuple*
    - A tuple return by `req_place_details(df, api_key)`

- **curr:** *str*
    - Name of the business
#
