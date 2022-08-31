# Written by Taj Bishop 22978883 25/08/2022
# This script creates a copy of armadale_cleaned.csv called armadale_cleaned_with_menu.csv 
# and scrapes Google Maps using selenium to update the Menu column of the CSV file

# Requires geckodriver: https://github.com/mozilla/geckodriver/releases
# Requires Firefox: https://www.mozilla.org/en-US/firefox/new/
# In order for this code to work, the Firefox tab must remain open, e.i., it cannot be minimized
# armadale_cleaned.csv must be in the same file as this script

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pandas
import os, sys
import os.path

def menu_scraper():
    GOOGLE_MAPS_URL = "https://www.google.com/maps/@-31.9431878,115.8819809,12.25z"

    # try open armadale_cleaned_with_menu
    try:
        data = pandas.read_csv(os.path.join(sys.path[0], "armadale_cleaned_with_menu.csv"), keep_default_na=False)
    except:
        # if above file not found, try open armadale_cleaned
        try:
            data = pandas.read_csv(os.path.join(sys.path[0], "armadale_cleaned.csv"), keep_default_na=False)
        except:
            print("Exception: armadale_cleaned.csv needs to exist in same folder as this script")

    # geckodriver.exe can be in either (1) system PATH (2) same folder as this script (3) same folder as python installation
    driver = webdriver.Firefox()

    # open Google Maps centred on Perth
    try:
        driver.get(GOOGLE_MAPS_URL)
    except:
        print("Exceptiopn: Could not access Google Maps. Ensure that device has stable internet connection.")

    row_index = -1
    for index, row in data.iterrows():
        # increment to the current row
        row_index += 1
        # if this row already contains a value for menu, move on to the next row
        business_menu = row[21]
        if business_menu != "":
            continue

        # enter business name and click search
        business_name = row[4]
        search_box = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, 'searchboxinput')))
        search_box.send_keys(business_name)
        search_button = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, 'searchbox-searchbutton')))
        search_button.click()

        ''' I need to add code to bypass the ads that occasionally show up in the drop down menu '''
        # wait 5 seonds to see if drop down menu appears: true -> click first result, fale -> ignore
        try:
            first_result = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, 'hfpxzc')))
            first_result.click()
        except TimeoutException:
            pass

        # interact with side panel so that the photo names load
        side_panel = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, 'DUwDvf.fontHeadlineLarge')))
        side_panel.click()
        
        # wait 4 seonds to see if location has photos: true -> get results, fale -> create empty results
        # code stops working if timer ends while in the middle of getting photo names
        photo_name_text = []
        try:
            photo_names = WebDriverWait(driver, 4).until(ec.visibility_of_all_elements_located((By.CLASS_NAME, 'fontTitleSmall.fontTitleMedium')))
            for photo_name in photo_names:
                photo_name_text.append(photo_name.text)
        except TimeoutException:
            pass
        
        # clear search box of business name
        search_box = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, 'searchboxinput')))
        search_box.clear()
        has_menu = "NO"
        for name in photo_name_text:
            if name == "Menu":
                has_menu = "YES"

        # print results
        print(business_name)
        print("Menu available:", has_menu)

        # update dataframe
        data.iloc[row_index, 21] = has_menu

        # update CSV file every 5 businesses
        n = row_index
        if (n % 5 == 0):
            data.to_csv(os.path.join(sys.path[0], "armadale_cleaned_with_menu.csv"), index=False)

    # once finished, quit Firefox
    driver.quit()

if __name__ == "__main__":
    menu_scraper()