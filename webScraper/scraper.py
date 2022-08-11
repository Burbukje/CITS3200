import pandas as pd
import numpy as np
import os
from urllib.parse import urlencode
import requests
from datetime import date
import csv

API_KEY = os.environ["PLACES_API"]

DATA_FILE = "test_files/Food Business Listing 2021.22 - CoA Summary.xls"


def get_business_name_add(file: str) -> dict:
    df = read_file(file)
    name_addr = dict()

    # Get the rows x column in tuple form
    shape = df.shape

    rows = shape[0]

    for i in range(rows):
        line = df.iloc[i, :]
        business_name = line["business_name"]
        addr = line["parcel_address"]
        name_addr[business_name] = addr

    return name_addr


def read_file(file: str) -> pd.DataFrame:
    '''
    Reads a xls or xlsx file

    Return:
        Pandas DataFrame
    '''
    # Read in the file
    data = pd.read_excel(file)

    # Drop all empty Rows
    data = data.dropna(how="all")

    # Replace nan with an empty string
    data = data.fillna("")

    # Define the headers
    data.columns = data.iloc[0]

    # Reset the index
    data.iloc[1:].reset_index(drop=True)

    # Clean headers, strip leading and trailing spaces. convert lowercase and replace spaces seperating words with a underscore 
    data.columns = data.columns.str.strip().str.lower().str.replace(" ", "_")

    # skip the first row, which is a copy of our column reference.
    data = data[1:]

    return data


get_business_name_add(DATA_FILE)