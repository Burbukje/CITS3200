# Written by Taj Bishop 22978883
# Demonstrates how selenium can be used to extract menu data from Google Maps
# Requires geckodriver: https://github.com/mozilla/geckodriver/releases
# Requires Firefox: https://www.mozilla.org/en-US/firefox/new/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

URLs = {
    "https://www.google.com/maps/place/Tasty+Momo+Restaurant+Nepalese+%26+Indian+Cuisine/@-31.9067571,115.8731062,15z/data=!4m5!3m4!1s0x2a32b075d9e1d36f:0x5179bbaeb7d8693c!8m2!3d-31.9067574!4d115.8818606",
    "https://www.google.com/maps/place/Naab+Restaurant/@-31.9070134,115.8801099,17z/data=!4m5!3m4!1s0x2a32b11187152f91:0xf4e765800be7b63d!8m2!3d-31.9080676!4d115.8813052",
    "https://www.google.com/maps/place/Curry+Thieves/@-31.89532,115.871346,18.26z/data=!4m5!3m4!1s0x0:0x2765e7d7f965fa3b!8m2!3d-31.8959657!4d115.8714174"
}

print("Note: I do not know why the URLs are checked in random order.")
print("The code should print 2 Trues and 1 False.")

# geckodriver.exe can be in either (1) system PATH (2) same folder as this script (3) same folder as python installation
driver = webdriver.Firefox()
# if the line above does not work, you can manually define where to find geckodriver.exe. For example:
# driver = webdriver.Firefox(executable_path=r'C:\Users\bisho\Documents\geckodriver.exe')

driver.implicitly_wait(4) # wait max 4 seconds to find an element not immediately available

for URL in URLs:
    driver.get(URL)
    answer = False

    try:
        elements = driver.find_elements(By.CLASS_NAME, 'fontTitleSmall.fontTitleMedium')
        for element in elements:
            if element.text == "Menu":
                answer = True

    except NoSuchElementException:
        print("Error: Cannot access Google Map's photos")
    
    print(answer)
    
driver.quit()