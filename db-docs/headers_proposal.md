# Cleaned Data Headers
## Author: Tom Nguyen <22914578>
### Version: 0.1
#

## Purpose
The purpose of this document is to simplify and define the headers for cleaned web scraped business data and to layout a plan for the Data Base Schema.

As Alexia had noted in the meeting (17/08/2022), many of the headers are redundant and we are able to make modifications without losing any key details.

## Proposal for new headers
A more detailed explaination will follow.

### [Table 1 (Year)](#table-1-year-1)
- Collection Year

### [Table 2 (LGA)](#)
- Local Government

### [Table 3 (Business)](#table-3-business-1)
- Business ID (Google Places ID)
- Business Name
- Notes

### [Table 4 (Classification)](#table-4-classification-1)
- Classification
- Category One
- Category Two
- Sub Category One
- Sub Category Two

### [Table 5 (Contact)](#table-5-contact-1)
- Longitude
- Latitude
- LGA Provided Address
- Formatted Address
- Contact
- Website
- Menu (maybe)
- Opening Hours

#

## Definition of headers

#

## Table 1 (Year)

#

### **Collection Year**
The year the data was collected

#### **Data Type**
- Integer
#### **Format**
- 2020
- 1901

#

## Table 2 (LGA)

#

### **Local Governement**
#### **Data Type**
- VARCHAR
#### **Format**
The standard format for LGA names will be "[Name], City of" or "[Name], Shire of"

For example "Armadale, City of". 

What we will NOT accept is "City of Armadale"

The reason for this is for ease of sorting in excel spread sheets

#

## Table 3 (Business)

#

### **Business ID (Google Places ID)**
Google Places assigns unique IDs to businesses. The advantage of storing the Place ID is that comparing and updating business data can be simplified. It is also possible for the same place or location to have multiple different IDs

**Dev Note:**
This ID should NOT be used as a relational key in the DB.

#### **Data Type**
- There is no maxium length for Place IDs
- VARCHAR
#### **Format**
Example:
- `ChIJgUbEo8cfqokR5lP9_Wh_DaM`
- `EicxMyBNYXJrZXQgU3QsIFdpbG1pbmd0b24sIE5DIDI4NDAxLCBVU0EiGhIYChQKEgnRTo6ixx-qiRHo_bbmkCm7ZRAN`

#

### **Business Name**
The name of the business.

**TODO:** Do we want to use the name given to us by the LGA or Google?

#### **Data Type**
- Varchar
#### **Format**
- `Child's Day Care`
- `The Beaufort`
- `Lot 619`

#

### **Notes**
Any notes the user wants to add

**TODO:**
Reconsider the size limit

#### **Data Type**
- Varchar (255)
#### **Format**
- [short text msg]

#

## Table 4 (Classification)

#

### **Classification**
A code. Defined in Appendix A: Food Business Classification Framework

#### **Data Type**
- Char (1)
#### **Format**
- A - F

#


### **Classification**
A code. Defined in Appendix A: Food Business Classification Framework

#### **Data Type**
- Char (1)
#### **Format**
Classification Code:
- A - F

#

#### **Category One**
A code. Defined in Appendix A: Food Business Classification Framework

#### **Data Type**
- Varchar (5)
#### **Format**
Category One:
- 1.00 - 14.00

Example
- [Classification Code] [Category One Code]
- A1.00
- E2.00

#

#### **Category One**
A code. Defined in Appendix A: Food Business Classification Framework

A business can fall under two categories

#### **Data Type**
- Varchar (5)
#### **Format**
Category One Code:
- 1.00 - 14.00

Example
- [Classification Code] [Category One Code]
- A1.00
- E2.00

#


#### **Category Two**
A code. Defined in Appendix A: Food Business Classification Framework

A business can fall under two categories

#### **Data Type**
- Varchar (5)
#### **Format**
Category Two Code:
- 1.00 - 14.00

Example
- [Classification Code] [Category One Code]
- A1.00
- E2.00

#

#### **Sub Category One**
A code. Defined in Appendix A: Food Business Classification Framework

A business can fall under two sub categories

#### **Data Type**
- Varchar (5)
#### **Format**
Category One:
- 0.00 - 0.32

Example:
- [Classification Code] [Category One Code] [Sub Category Code]
- A1.02
- E2.12

#

#### **Sub Category Two**
A code. Defined in Appendix A: Food Business Classification Framework

A business can fall under two sub categories

#### **Data Type**
- Varchar (5)
#### **Format**
Category One:
- 0.00 - 0.32

Example:
- [Classification Code] [Category One Code] [Sub Category Code]
- A1.03
- E2.32

#

## Table 5 (Contact)

#

#### **Longitude**
The geographic coordinate of the business

#### **Data Type**
- Float
#### **Format**
- 151.199025

#

#### **Latitude**
The geographic coordinate of the business

#### **Data Type**
- Float
#### **Format**
- 151.199025

#

#### **LGA Provided Address**
Address provided by the LGA

#### **Data Type**
- Varchar
#### **Format**
- 31 Lowood Road, Mount Barker

#

#### **Formatted Address**
Provided by the Google Places API

#### **Data Type**
- Varchar
#### **Format**
- Shop 16/10 Langton Road, Mount Barker

#

#### **Contact**
A phone number provided by Googel Place API

#### **Data Type**
- Integer (Maybe? or varchar?)
#### **Format**
- 0892735517 (Integer)
- `(08) 9863 2334` (varchar)

#

#### **Website**
A website provided by Googel Place API

It is common to have business using facebook as their website. Google Places API does not return these results.

**NOTE:**
We may want to look into Facebook API

#### **Data Type**
- Varchar
#### **Format**
- `https://www.karribank.com.au/bar`
- `https://www.facebook.com/cateringandcafe/about`

#

#### **Opening Hours**
The Opening hours provided by Google API


#### **Data Type**
- Blob or Tinyblob
#### **Format**
- TODO: The documentation for the format

#