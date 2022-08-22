import scraper
import unittest
import pandas as pd
import sys

class TestScraper(unittest.TestCase):
    name_addr = dict()
    df = pd.DataFrame()
    headers = None

    skip_api_test = True


    DATA_FILE = "./test_files/inputs/Food Business Listing 2021.22 - CoA Summary.xls"

    cider_house_test = {
        "name":  "The Naked Apple Cider House (formerly Hopsscotch Restaurant)",
        "addr":  "1088 Brookton Highway KARRAGULLEN WA 6111", 
        "id":    'ChIJ32AGNJHrMioR_PeUI_UpN6A'}


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


    def test_cleaned_headers(self):
        headers = scraper.HEADERS
        expected_headers = list()
        with open("./test_files/headers/headers_cleaned.txt", "r") as f:
            for line in f:
                expected_headers.append(line.strip())

        for index, head in enumerate(expected_headers):
            self.assertTrue(headers.index(head) == index, msg=f'Failed at {head}')


    #TODO: add more tests
    @unittest.skipIf(skip_api_test, "API: basic info test not run")
    def test_request_basic_info(self):
        cider_house_expected_basic = {
            'candidates': [{   'formatted_address': '1088 Brookton Hwy, Karragullen WA 6111, Australia', 
                                'geometry': {   'location': {   'lat': -32.096721, 'lng': 116.1041666}, 
                                                'viewport': {   'northeast': {'lat': -32.09529222010727, 'lng': 116.1054979798927}, 
                                                                'southwest': {'lat': -32.09799187989271, 'lng': 116.1027983201073}}
                                            },
                                'name': 'Naked Apple Cider House', 
                                'place_id': 'ChIJ32AGNJHrMioR_PeUI_UpN6A', 
                                'types': ['restaurant', 'food', 'point_of_interest', 'establishment']
                            }], 
            'status': 'OK'
        }

        response = scraper.request_basic_info(self.cider_house_test["name"], self.cider_house_test["addr"])

        self.assertTrue(isinstance(response, type(dict())), msg=f"Expected a JSON or Dictionary object. got {type(response)}")
        

    # TODO: add more tests
    @unittest.skipIf(skip_api_test, "API: contact info test not run")
    def test_request_contact_info(self):
        cider_house_expected_contact = {
                'html_attributions': [], 
                'result': { 'formatted_phone_number': '(08) 9496 1138', 
                            'opening_hours': {'open_now': True, 
                                              'periods': [  {'close': {'day': 0, 'time': '1900'}, 'open': {'day': 0, 'time': '1100'}}, 
                                                            {'close': {'day': 3, 'time': '1530'}, 'open': {'day': 3, 'time': '1130'}}, 
                                                            {'close': {'day': 4, 'time': '2100'}, 'open': {'day': 4, 'time': '1130'}}, 
                                                            {'close': {'day': 5, 'time': '2200'}, 'open': {'day': 5, 'time': '1130'}}, 
                                                            {'close': {'day': 6, 'time': '2200'}, 'open': {'day': 6, 'time': '1100'}}], 
                                                'weekday_text': ['Monday: Closed', 'Tuesday: Closed', 'Wednesday: 11:30 AM – 3:30 PM', 'Thursday: 11:30 AM – 9:00 PM', 'Friday: 11:30 AM – 10:00 PM', 'Saturday: 11:00 AM – 10:00 PM', 'Sunday: 11:00 AM – 7:00 PM']}, 
                            'website': 'http://www.nakedapple.com.au/'}, 
                'status': 'OK'
        }

        response = scraper.request_contact_info(self.cider_house_test["id"])

        self.assertTrue(isinstance(response, type(dict())), msg=f"Expected a JSON or Dictionary object. got {type(response)}")


    # TODO: add more tests
    @unittest.skipIf(skip_api_test, "API: place details test not run")
    def test_req_place_details(self):
        return
        

    #TODO
    def test_fill_empty(self):
        test_10 = scraper.fill_empty(10)

        self.assertTrue(len(test_10) == 10, msg=f"Expected: 10 Got: {len(test_10)}")

    #TODO
    def test_get_formatted_addr(self):
        basic_data =\
            [{
                "candidates": 
                [
                    {
                        "formatted_address": "1311 Brookton Hwy, Karragullen WA 6111, Australia", 
                        "geometry": 
                            {  
                                "location": {"lat": -32.1060737, "lng": 116.1236113}, 
                                "viewport": 
                                    {   
                                        "northeast": {"lat": -32.10493117010727, "lng": 116.1246861798927}, 
                                        "southwest": {"lat": -32.10763082989272, "lng": 116.1219865201073}
                                    }
                            }, 
                        "name": "Karragullen Fruit Company (S&C Fiolo)", 
                        "place_id": "ChIJm2OAe_frMioR1jrCFR8u0r4", 
                        "types": ["point_of_interest", "establishment"]
                    }
                ], 
                "status": "OK"
            },
            {
                "html_attributions": [], 
                "result": 
                    {
                        "formatted_phone_number": "(08) 9397 5958", 
                        "opening_hours": 
                            {
                                "open_now": False, 
                                "periods": 
                                    [
                                        {
                                            "close": {"day": 1, "time": "1700"}, 
                                            "open": {"day": 1, "time": "0800"}}, 
                                            {"close": {"day": 2, "time": "1700"}, 
                                            "open": {"day": 2, "time": "0800"}}, 
                                            {"close": {"day": 3, "time": "1700"}, 
                                            "open": {"day": 3, "time": "0800"}}, 
                                            {"close": {"day": 4, "time": "1700"}, 
                                            "open": {"day": 4, "time": "0800"}}, 
                                            {"close": {"day": 5, "time": "1700"}, 
                                            "open": {"day": 5, "time": "0800"}}, 
                                            {"close": {"day": 6, "time": "1600"}, 
                                            "open": {"day": 6, "time": "0800"}}], 
                                            "weekday_text": 
                                                [
                                                    "Monday: 8:00 AM – 5:00 PM", 
                                                    "Tuesday: 8:00 AM – 5:00 PM", 
                                                    "Wednesday: 8:00 AM – 5:00 PM", 
                                                    "Thursday: 8:00 AM – 5:00 PM", 
                                                    "Friday: 8:00 AM – 5:00 PM", 
                                                    "Saturday: 8:00 AM – 4:00 PM", 
                                                    "Sunday: Closed"
                                                ]
                            }
                    }, 
                "status": "OK"
            }]

        address = scraper.get_formatted_addr(basic_data).split()

        print(address[0])

if __name__ == '__main__':
    unittest.main(verbosity=2)