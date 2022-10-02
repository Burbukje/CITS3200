# Documentation for Database 

## Purpose 
The purpose of this document is to describe the tables : 
- table names 
- columns 
- expected types 
- expected input 

# 

## Table 1 : webScraper_business 
- id 
- business_name 
- notes 
- local_government_area_id 
- webScraper_local_government 

## Table 2 : webScraper_classification 
- id 
- classification 
- business_id_id 
- webScraper_business 
- category_one 
- category_three 
- category_two 
- sub_cat_three 
- sub_cat_two 
- sub_cat_one 

## Table 3 : webScraper_collection_year
- year 

## Table 4 : webScraper_contact_details
- id 
- longitude 
- latitude 
- parcel_address 
- formatted_address 
- phone 
- website 
- menu 
- opening_hours 
- business_id_id 
- webScraper_business 

## Table 5 : webScraper_local_government
- local_government_area
- year_id
- webScraper_collection_year

#

## Table 1 : webScraper_business 
About Table :  Each record represents a food business

Columns : 

### id 
Description of field : unique identifier for that business

Expected type : varchar(32) 

Expected input : 

### business_name 
Description of field : name of business 

Expected type : varchar(128) 

Expected input : 
- Gilbert Wines
- Plantagenet Wines

### notes 
Description of field : Notes the user would potentially want to add

Expected type : text 

Expected input : 
- another email they provided is wine@plantagenetwines.com
- no phone number, website or email provided

### local_government_area_id 
Description of field : foreign key referencing the "local_government_area" field from the webScraper_local_government table 

Expected type : varchar(128) 

Expected input : 

# 

## Table 2 : webScraper_classification 
About Table : Stores the different types of organisations 

Columns : 

### id 
Description of field : unique identifier for each type of organisation 

Expected type : integer 

Expected input : 

### classification 
Description of field : A code representing each type of organisation. Defined in Appendix A : Food Business Classification Framework. 

Expected type : varchar(1) 

Expected input : A - F 

### business_id_id 
Description of field : foreign key referencing the "id" field from the webScraper_business table.  

Expected type : char(32) 

Expected input : 

### category_one 
Description of field : 

Expected type : decimal 

Expected input : 

### category_three 
Description of field : 

Expected type : decimal 

Expected input : 

### category_two 
Description of field : 

Expected type : decimal 

Expected input : 

### sub_cat_one 
Description of field : 

Expected type : decimal 

Expected input : 

### sub_cat_three 
Description : 

Expected type : decimal 

Expected input : 

### sub_cat_two 
Description : 

Expected type : decimal 

Expected input : 

# 

## Table 3 : webScraper_collection_year 
About Table : Stores the years in which data was collected

Columns : 

### year 
Description : The year the data was collected

Expected type : integer 

Expected input 
- 2020
- 1976 

# 

## Table 4 : webScraper_contact_details 
About Table : This table represents the contact details and location of a business

Columns : 

### id 
Description : unique identifier for each record

Expected type : integer 

Expected input : 

### longitude 
Description : the geographic coordinate of the business

Expected type : decimal 

Expected input : 151.199025

### latitude 
Description : the geographic coordinate of the business

Expected type : decimal 

Expected input : 151.199025

### parcel_address 
Description : 

Expected type : varchar(128) 

Expected input : 
- 1 Carradine Road BEDFORDALE WA 6112
- 169 South Western Highway ARMADALE WA 6112
- 39 Seville Drive SEVILLE GROVE WA 6112

### formatted_address 
Description : provided by the Google Places API

Expected type : varchar(128) 

Expected input : 
- Shop 16/10 Langton Road, Mount Barker

### phone 
Description : phone number to contact business 

Expected type : varchar(15) 

Expected input : 
- 0898531123
- 0862433913
- 0898491132

### website 
Description : webpage link for a food business

Expected type : varchar(128) 

Expected input : 
- https://www.karribank.com.au/bar
- https://www.facebook.com/cateringandcafe/about

### menu 
Description : shows if a food business provides a menu

Expected type : bool 

Expected input : 
- Yes, provided on website
- No

### opening_hours 
Description : the opening hours provided by Google API

Expected type : text 

Expected input : 

### business_id_id 
Description : foreign key that references the "id" field of the webScraper_business table

Expected type : char(32) 

Expected input : 

# 

## Table 5 : webScraper_local_government 
About Table : each record of this table represents a local government area

Columns : 

### local_government_area 
Description : 

Expected type : varchar(128) 

Expected input : 
The standard format for LGA names will be "[Name], City of" or "[Name], Shire of"

For example "Armadale, City of".

What we will NOT accept is "City of Armadale"

The reason for this is for ease of sorting in excel spread sheets

### year_id 
Description : foreign key referencing the "year" field in the webScraper_collection_year table

Expected type : integer 

Expected input : 
- 2020
- 1992 

# 







