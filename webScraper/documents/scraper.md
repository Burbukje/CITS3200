# Food Atlas - Scraper Module


## [Processing inputs](#processing-inputs-1)
- [Headers](#headers)
- [Processing xls and slsx input files](#routines)

## [API Requests](#api-requests-1)
- [Requesting both basic information and contact details](#routines-1)
- [Basic Information](#routines-1)
- [Contact Details](#routines-1)

## [Extracting Data from API response]()
- [Formatted Address]()
- [Lattitudes and Longitudes]()
- [Business Type]()
- [Phone Number]()
- [Opening Hours]()
- [Website]()


## [Creating a csv file]()


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

Data requested include:

Basic Information:
- Google Places unique id
- Formated Address
- location (longitude and latitudes)
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
