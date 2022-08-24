CREATE TABLE Classification
(
  classification_code CHAR NOT NULL,
  classification_type VARCHAR NOT NULL,
  description VARCHAR NOT NULL,
  PRIMARY KEY (classification_code)
);

CREATE TABLE Category
(
  category_type VARCHAR NOT NULL,
  category_code VARCHAR NOT NULL,
  description VARCHAR NULL,
  classification_code CHAR NOT NULL,
  PRIMARY KEY (category_code),
  FOREIGN KEY (classification_code) REFERENCES Classification(classification_code)
);

CREATE TABLE Sub-category
(
  sub-category_type VARCHAR NOT NULL,
  sub-category_code VARCHAR NOT NULL,
  description VARCHAR NOT NULL,
  examples VARCHAR NOT NULL,
  category_code VARCHAR NOT NULL,
  PRIMARY KEY (sub-category_code),
  FOREIGN KEY (category_code) REFERENCES Category(category_code)
);