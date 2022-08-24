CREATE TABLE Food_Business
(
  local_government_area TEXT NOT NULL,
  red_cap_id INTEGER NOT NULL,
  business_id INTEGER PRIMARY KEY NULL,
  collection_year INTEGER NOT NULL,
  business_name TEXT NOT NULL,
  notes TEXT NULL, 
  contact_1 INTEGER NULL,
  contact_2 INTEGER NULL,
  email TEXT NULL,
  website TEXT NULL,
  menu_provided INTEGER NOT NULL,
  children_menu_provided INTEGER NOT NULL,
  mon_open TEXT NOT NULL,
  mon_close TEXT NOT NULL,
  mon_total_hrs TEXT NOT NULL,
  tue_open TEXT NOT NULL,
  tue_close TEXT NOT NULL,
  tue_total_hrs TEXT NOT NULL,
  wed_open TEXT NOT NULL,
  wed_close TEXT NOT NULL,
  wed_total_hrs TEXT NOT NULL,
  thu_open TEXT NOT NULL,
  thu_close TEXT NOT NULL,
  thu_total_hrs TEXT NOT NULL,
  fri_open TEXT NOT NULL,
  fri_close TEXT NOT NULL,
  fri_total_hrs TEXT NOT NULL,
  sat_open TEXT NOT NULL,
  sat_close TEXT NOT NULL,
  sat_total_hrs TEXT NOT NULL,
  sun_open TEXT NOT NULL,
  sun_close TEXT NOT NULL,
  sun_total_hrs TEXT NOT NULL,
  total_weekdays_hrs TEXT NOT NULL,
  total_weekend_hrs TEXT NOT NULL
);

CREATE TABLE Business_Address
(
  y_latitude INTEGER NULL,
  x_longitude INTEGER NULL,
  original_lga_provided_address TEXT PRIMARY KEY NOT NULL,
  new_unit_shop_number INTEGER NULL,
  new_street_number INTEGER NOT NULL,
  new_street_name TEXT NOT NULL,
  new_street_type TEXT NOT NULL,
  new_street_suffix TEXT NULL,
  new_suburb TEXT NOT NULL,
  new_postcode INTEGER NOT NULL,
  Business_ID INTEGER NULL,
  FOREIGN KEY (Business_ID) REFERENCES Food_Business(Business_ID)
);

CREATE TABLE Category
(
  Classification TEXT NOT NULL,
  Category TEXT NOT NULL,
  Category_code INTEGER PRIMARY KEY NOT NULL,
  Sub_category TEXT NULL,
  Sub_category_code INTEGER NULL,
  Descriptrion_and_example TEXT NOT NULL,
  Business_ID INTEGER NULL,
  FOREIGN KEY (Business_ID) REFERENCES Food_Business(Business_ID)
);
