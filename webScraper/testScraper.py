import scraper
import unittest
import pandas as pd

class TestGetBusinessNameAdder(unittest.TestCase):
    df = pd.DataFrame()

    def setUp(self):
        DATA_FILE = "./test_files/Food Business Listing 2021.22 - CoA Summary.xls"
        self.df = scraper.get_business_name_add(DATA_FILE)

    def test_get_name(self):
        self.assertEqual(self.df["Armadale Primary School Canteen"], "1 Carradine Road BEDFORDALE WA 6112")
        self.assertEqual(self.df["Snugglepot Child Care Centre"], "48 Poad Street SEVILLE GROVE WA 6112")
        self.assertEqual(self.df["Ashlee's Family Daycare"], "")
        self.assertEqual(self.df["S and C Fiolo"], "1311 Brookton Highway KARRAGULLEN WA 6111")
        self.assertEqual(self.df["Zeez Beez"], "")


if __name__ == '__main__':
    unittest.main()