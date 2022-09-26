from django.test import TestCase
from webScraper.models import Collection_Year, Contact_Details, Business, Local_Government, Classification
from webScraper.classification_enums import *
import decimal

# Create your tests here.

class BusinessTests(TestCase):
    def setUp(self) -> None:
        self.coll_year = Collection_Year.objects.create(year=2022)
        self.local_gov = Local_Government.objects.create(year=self.coll_year, local_government_area="Armadale, City of")
        self.business = Business.objects.create(local_government_area=self.local_gov, business_name="Armadale Primary School Canteen", notes="This is a test 12345")
        
        self.hours = {"weekday_text": [
                    "Monday: 7:30 AM \u2013 5:30 PM",
                    "Tuesday: 7:30 AM \u2013 5:30 PM",
                    "Wednesday: 7:30 AM \u2013 5:30 PM",
                    "Thursday: 7:30 AM \u2013 5:30 PM",
                    "Friday: 7:30 AM \u2013 5:30 PM",
                    "Saturday: Closed",
                    "Sunday: Closed"
                ]}
        
        self.contact = Contact_Details.objects.create(   business_id=self.business, 
                                                    longitude= 116.0262646,
                                                    latitude= -32.1476309,
                                                    parcel_address="1 Carradine Road BEDFORDALE WA 6112",
                                                    formatted_address="1 Carradine Rd, Mount Nasura WA 6112, Australia",
                                                    phone="(08) 9391 4500",
                                                    website="http://armadaleps.wa.edu.au",
                                                    menu=False,
                                                    opening_hours=self.hours
                                                )

        
        self.classification = Classification.objects.create(business_id=self.business)

    def test_year(self) -> None:
        obj = Collection_Year.objects.get(year=2022)
        self.assertEqual(obj.year, 2022)
        self.assertEqual(obj.get_year(), 2022)
        


    def test_local_government(self) -> None:
        obj = Local_Government.objects.get(local_government_area="Armadale, City of")
        self.assertEqual(obj.local_government_area, "Armadale, City of")
        self.assertNotEqual(obj.local_government_area, "armadale, city of")
        self.assertEqual(obj.year.year, 2022)
        self.assertEqual(obj.year.get_year(), 2022)
        self.assertEqual(obj.get_lga(), "Armadale, City of")



    def test_business(self) -> None:
        obj = Business.objects.all()[0]
        self.assertEqual(obj.business_name, "Armadale Primary School Canteen")
        self.assertNotEqual(obj.business_name, "armadale primary school canteen")
        self.assertEqual(obj.notes, "This is a test 12345")
        self.assertNotEqual(obj.notes, "This is a test 123")

        self.assertEqual(obj.get_name(), "Armadale Primary School Canteen")
        self.assertEqual(obj.get_notes(), "This is a test 12345")


    def test_contacts(self) -> None:
        obj = Contact_Details.objects.all()[0]
        self.assertEquals(obj.business_id, self.business)
        self.assertAlmostEqual(obj.longitude, decimal.Decimal(float(116.0262646)))
        self.assertAlmostEqual(obj.latitude, decimal.Decimal(float(-32.1476309)))
        self.assertEquals(obj.parcel_address, "1 Carradine Road BEDFORDALE WA 6112")
        self.assertEquals(obj.formatted_address, "1 Carradine Rd, Mount Nasura WA 6112, Australia")
        self.assertEquals(obj.phone, "(08) 9391 4500")
        self.assertEquals(obj.website, "http://armadaleps.wa.edu.au")
        self.assertEquals(obj.menu, False)
        self.assertEquals(obj.opening_hours, self.hours)
        

    def test_classification(self) -> None:
        obj = Classification.objects.all()[0]
        self.assertEquals(obj.classification, 'None')
        obj.classification = Classification_Appendix.E

        obj.category_one = Category_A.BAKERY

        self.assertEquals(obj.business_id, self.business)
        self.assertEquals(obj.business_id.id, self.business.id)
        self.assertEquals(obj.classification, 'E')
        self.assertEquals(obj.category_one, '7.0')