CREATE TABLE business
(
  collection_year INT NOT NULL,
  PRIMARY KEY (collection_year)
);

CREATE TABLE lga
(
  local_gov VARCHAR NOT NULL,
  collection_year INT NOT NULL,
  PRIMARY KEY (local_gov),
  FOREIGN KEY (collection_year) REFERENCES business(collection_year)
);

CREATE TABLE business
(
  business_place_id VARCHAR NOT NULL,
  name VARCHAR NOT NULL,
  notes VARCHAR(255) NOT NULL,
  internal_id INT NOT NULL,
  opening_hours  NOT NULL,
  local_gov VARCHAR NOT NULL,
  PRIMARY KEY (internal_id),
  FOREIGN KEY (local_gov) REFERENCES lga(local_gov)
);

CREATE TABLE classification
(
  class CHAR(1) NOT NULL,
  internal_id INT NOT NULL,
  FOREIGN KEY (internal_id) REFERENCES business(internal_id)
);

CREATE TABLE contact
(
  longitude FLOAT NOT NULL,
  latitude FLOAT NOT NULL,
  lga_address VARCHAR NOT NULL,
  formatted_address VARCHAR NOT NULL,
  phone VARCHAR NOT NULL,
  website VARCHAR NOT NULL,
  New_Column INT NOT NULL,
  internal_id INT NOT NULL,
  FOREIGN KEY (internal_id) REFERENCES business(internal_id)
);