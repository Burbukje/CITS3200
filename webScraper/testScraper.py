import scraper
import unittest
import pandas as pd

class TestScraper(unittest.TestCase):
    name_addr = dict()
    df = pd.DataFrame()
    headers = None

    DATA_FILE = "./test_files/Food Business Listing 2021.22 - CoA Summary.xls"

    def setUp(self):
        self.name_addr = scraper.get_business_name_add(self.DATA_FILE)
        self.df =scraper.read_file(self.DATA_FILE)
        self.headers = self.df.keys()


    def test_correct_type(self):
        self.assertTrue(isinstance(self.name_addr, type(dict())), msg=f"Business name and address object is NOT a dictionary type")
        self.assertTrue(isinstance(self.headers, pd.Index), msg=f"Headers object is NOT a Pandas Index type")
        self.assertTrue(isinstance(self.df, pd.DataFrame), msg=f"df object is NOT a Pandas DataFrame type")


    def test_get_name_addr(self):
        self.assertEqual(self.name_addr["Armadale Primary School Canteen"], "1 Carradine Road BEDFORDALE WA 6112")
        self.assertEqual(self.name_addr["Snugglepot Child Care Centre"], "48 Poad Street SEVILLE GROVE WA 6112")
        self.assertEqual(self.name_addr["Ashlee's Family Daycare"], "")
        self.assertEqual(self.name_addr["S and C Fiolo"], "1311 Brookton Highway KARRAGULLEN WA 6111")
        self.assertEqual(self.name_addr["Zeez Beez"], "")


    def test_headers(self):
        expected = ['account', 'business_name', 'property_description', 'parcel_address',
                    'street_name', 'suburb', 'premises_type']
        
        for key in self.headers:
            expected_in_keys = False
            if key in expected:
                expected_in_keys = True
            self.assertTrue(expected_in_keys, msg=f"{key} not in expected list")


    def test_fail_headers(self):
        expected = ["Dont sue me", "Debug"]
        
        for key in self.headers:
            expected_in_keys = True
            if not key in expected:
                expected_in_keys = False
            self.assertFalse(expected_in_keys, msg=f"{key} is in empty list")

if __name__ == '__main__':
    unittest.main()