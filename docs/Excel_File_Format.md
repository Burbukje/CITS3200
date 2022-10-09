# Food Atlas File Format

### Author: Tom Nguyen

### Purpose: UWA CITS3200 Food Atlas project

# 

This document will detail the required format of column names. If the column names are not in line with the standards this document lays out the web scraping program and upload functions will fail.

## Excel
The column names must be present in the excel file but the order of the columns do not matter, you may also have extra columns, the food atlas will simply ignore the extra columns.

You may leave some rows blanks but this will effect the efficiency of the web scraper for data collection. 

General Rule: Spaces in the column names are to be replaced by "_" (underscore).

## Columns

### 1. Business Name (Required):
- Column name: 
    - **business_name**
- Value: The name of the business e.g.
    - Child's Day Care
    - The Beaufort
    - Lot 619

### 2. Parcel Address (Optional):
- Column name: 
    - **parcel_address**
- Value: An address, Format does not matter e.g.
    - Shop 16/10 Langton Road, Mount Barker

### 3. Email (Optional)
- Column name:
    - **email**
- Value: A standard email address e.g.
    - admin@hotmail.com
    - test123@fakemail.com

## Example of valid Excel sheets

These are some examples of valid excel files:

![](./Screenshot%202022-10-05%20144242.png)

![](./Screenshot%202022-10-05%20143716.png)


