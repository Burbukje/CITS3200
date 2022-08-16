# Food Atlas - Scraper Module


## [Processing inputs](#processing-inputs-1)
- [Headers](#headers)
- [Processing xls and slsx input files](#processing-excel-sheets)

## [API Requests](#api-requests-1)
- [Requesting both basic information and contact details]()
- [Basic Information]()
- [Contact Details]()

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

## Processing Excel Sheets
- Currently this program does not support multiple pages. Thus please keep one page per file.

#
**Routines**

`read_file(file)`
- Reads in a excel file and returns a pandas Dataframe

**Parameters:**
- **file:** *string*
    - directory to the file

#

# API Requests
In this module we will be using Googles Places Api to request information on a business.

Data requested include:
- Google Places unique id
- Formated Address
- location (longitude and latitudes)
- Business Name
- Business Type
- Phone Number
- Opening Hours
- Website

# 

**Routines**

`