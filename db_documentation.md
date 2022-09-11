# Documentation for Database 

## Purpose 
The purpose of this document is to describe the tables : 
- table names 
- columns 
- expected types 
- expected input 

# 

## Table : auth_group 
Columns : 

### id 
expected type : integer 
expected input : 

### name 
expected type : varchar(150) 
expected input : 

# 

## Table : auth_group_permissions 
Columns : 

### id 
expected type : integer 
expected input : 

### group_id 
expected type : integer 
expected input : 

### permission_id 
expected type : integer 
expected input : 

# 

## Table : auth_permission 
Columns : 

### id 
expected type : integer 
expected input : 

### content_type_id 
expected type : integer 
expected input : 

### codename 
expected type : varchar(100) 
expected input : 

### name 
expected type : varchar(255) 
expected input : 

# 

## Table : auth_user 
Columns : 

### id 
expected type : integer 
expected input : 

### password 
expected type : varchar(128) 
expected input : 

### last_login 
expected type : datetime 
expected input : 

### is_superuser 
expected type : bool 
expected input : 

### username 
expected type : varchar(150) 
expected input : 

### last_name 
expected type : varchar(150) 
expected input : 

### email 
expected type : varchar(254) 
expected input : 

### is_staff 
expected type : bool 
expected input : 

### is_active 
expected type : bool 
expected input : 

### date_joined 
expected type : datetime 
expected input : 

### first_name 
expected type : varchar(150) 
expected input : 

# 

## Table : auth_user_group 
Columns : 

### id 
expected type : integer 
expected input : 

### user_id 
expected type : integer 
expected input : 

### group_id 
expected type : integer 
expected input : 

# 

## Table : auth_user_user_permissions 
Columns : 

### id 
expected type : integer 
expected input : 

### user_id 
expected type : integer 
expected input : 

### permission_id 
expected type : integer 
expected input : 

# 

## Table : django_admin_log 
Columns : 

### id 
expected type : integer 
expected input : 

### object_id 
expected type : text 
expected input : 

### object_repr 
expected type : varchar(200) 
expected input : 

### action_flag 
expected type : smallint 
expected input : 

### change_message 
expected type : text 
expected input : 

### content_type_id 
expected type : integer 
expected input : 

### user_id 
expected type : integer 
expected input : 

### action_time 
expected type : datetime 
expected input : 

# 

## Table : django_content_type 
Columns : 

### id 
expected type : integer 
expected input : 

### app_label 
expected type : varchar(100) 
expected input : 

### model 
expected type : varchar(100) 
expected input : 

# 

## Table : django_migrations 
Columns : 

### id 
expected type : integer 
expected input : 

### app 
expected type : varchar(255) 
expected input : 

### name 
expected type : varchar(255) 
expected input : 

### applied 
expected type : datetime 
expected input : 

# 

## Table : django_session 
Columns : 

### session_key 
expected type : varchar(40) 
expected input : 

### session_data 
expected type : text 
expected input : 

### expire_date 
expected type : datetime 
expected input : 

# 

## Table : webScraper_business 
Columns : 

### id 
expected type : varchar(32) 
expected input : 

### business_name 
expected type : varchar(128) 
expected input : 

### notes 
expected type : text 
expected input : 

### local_government_area_id 
expected type : varchar(128) 
expected input : 

# 

## Table : webScraper_classification 
Columns : 

### id 
expected type : integer 
expected input : 

### classification 
expected type : varchar(1) 
expected input : 

### business_id_id 
expected type : char(32) 
expected input : 

### category_one 
expected type : decimal 
expected input : 

### category_three 
expected type : decimal 
expected input : 

### category_two 
expected type : decimal 
expected input : 

### sub_cat_one 
expected type : decimal 
expected input : 

### sub_cat_three 
expected type : decimal 
expected input : 

### sub_cat_two 
expected type : decimal 
expected input : 

# 

## Table : webScraper_collection_year 
Columns : 

### year 
expected type : integer 
expected input : 

# 

## Table : webScraper_contact_details 
Columns : 

### id 
expected type : integer 
expected input : 

### longitude 
expected type : decimal 
expected input : 

### latitude 
expected type : decimal 
expected input : 

### parcel_address 
expected type : varchar(128) 
expected input : 

### formatted_address 
expected type : varchar(128) 
expected input : 

### phone 
expected type : varchar(15) 
expected input : 

### website 
expected type : varchar(128) 
expected input : 

### menu 
expected type : bool 
expected input : 

### opening_hours 
expected type : text 
expected input : 

### business_id_id 
expected type : char(32) 
expected input : 

# 

## Table : webScraper_local_government 
Columns : 

### local_government_area 
expected type : varchar(128) 
expected input : 

### year_id 
expected type : integer 
expected input : 

# 







