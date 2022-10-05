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

### business_name 
Description of field : name of business 

Expected type : varchar(128) 

Expected input : 
- Gilbert Wines
- Plantagenet Wines

### notes 
Description of field : Notes the user would potentially want to add

Expected type : text 

### local_government_area_id 
Description of field : foreign key referencing the "local_government_area" field from the webScraper_local_government table 

Expected type : varchar(128) 

# 

## Table 2 : webScraper_classification 
About Table : Stores the different types of organisations 

Columns : 

### id 
Description of field : unique identifier for each type of organisation 

Expected type : integer 

### classification 
Description of field : A code representing each type of organisation. Defined in Appendix A : Food Business Classification Framework. 

Expected type : varchar(1) 

### business_id_id 
Description of field : foreign key referencing the "id" field from the webScraper_business table.  

Expected type : char(32) 

### category_one 
Description of field : 

Expected type : decimal 

### category_three 
Description of field : 

Expected type : decimal 

### category_two 
Description of field : 

Expected type : decimal 

### sub_cat_one 
Description of field : 

Expected type : decimal 

### sub_cat_three 
Description : 

Expected type : decimal 

### sub_cat_two 
Description : 

Expected type : decimal 

# 

## Table 3 : webScraper_collection_year 
About Table : Stores the years in which data was collected

Columns : 

### year 
Description : The year the data was collected

Expected type : integer 

# 

## Table 4 : webScraper_contact_details 
About Table : This table represents the contact details and location of a business

Columns : 

### id 
Description : unique identifier for each record

Expected type : integer 

### longitude 
Description : the geographic coordinate of the business

Expected type : decimal 

### latitude 
Description : the geographic coordinate of the business

Expected type : decimal 

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

### phone 
Description : phone number to contact business 

Expected type : varchar(15) 

### website 
Description : webpage link for a food business

Expected type : varchar(128) 

### menu 
Description : shows if a food business provides a menu

Expected type : bool 

### opening_hours 
Description : the opening hours provided by Google API

Expected type : text 

### business_id_id 
Description : foreign key that references the "id" field of the webScraper_business table

Expected type : char(32) 

# 

## Table 5 : webScraper_local_government 
About Table : each record of this table represents a local government area

Columns : 

### local_government_area 
Description : 

Expected type : varchar(128) 

### year_id 
Description : foreign key referencing the "year" field in the webScraper_collection_year table

Expected type : integer 

# 







