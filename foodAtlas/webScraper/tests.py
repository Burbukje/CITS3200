from django.test import TestCase
from webScraper.models import Collection_Year, Contact_Details, Business, Local_Government

# Create your tests here.

class BussinessTests(TestCase):
    def setUp(self) -> None:
        coll_year = Collection_Year.objects.create(year=2022)
        local_gov = Local_Government.objects.create(year=coll_year, local_government_area="Armadale, City of")


    def test_year(self) -> None:
        obj = Collection_Year.objects.get(year=2022)
        self.assertEqual(obj.year, 2022)


    def test_local_government(self) -> None:
        obj = Local_Government.objects.get(local_government_area="Armadale, City of")
        self.assertEqual(obj.local_government_area, "Armadale, City of")
        self.assertNotEqual(obj.local_government_area, "armadale, city of")

        self.assertEqual(obj.year.year, 2022)
