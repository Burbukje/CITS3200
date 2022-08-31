# CITS3200

This script creates a copy of 'armadale_cleaned.csv' called 'armadale_cleaned_with_menu.csv' and scrapes Google Maps using selenium to update the Menu column of the CSV file. If the latter file already exists, then the code will continue to add information for the rows where Menu is empty.
Requires geckodriver: https://github.com/mozilla/geckodriver/releases
Requires Firefox: https://www.mozilla.org/en-US/firefox/new/

# In order for the code to work:
- Geckodriver must be in PATH environment variable
- the Firefox tab must remain open, e.i., it cannot be minimized
- armadale_cleaned.csv must be in the same file as this script
