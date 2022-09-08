CREATE TABLE classification
(
  classification_code CHAR NOT NULL,
  classification_type VARCHAR NOT NULL,
  description VARCHAR NOT NULL,
  PRIMARY KEY (classification_code)
);

CREATE TABLE category
(
  category_type VARCHAR NOT NULL,
  category_code VARCHAR NOT NULL,
  description VARCHAR NULL,
  classification_code CHAR NOT NULL,
  PRIMARY KEY (category_code),
  FOREIGN KEY (classification_code) REFERENCES classification(classification_code)
);

CREATE TABLE sub_category
(
  sub_category_type VARCHAR NOT NULL,
  sub_category_code VARCHAR NOT NULL,
  description VARCHAR NOT NULL,
  examples VARCHAR NOT NULL,
  category_code VARCHAR NOT NULL,
  PRIMARY KEY (sub_category_code),
  FOREIGN KEY (category_code) REFERENCES category(category_code)
);