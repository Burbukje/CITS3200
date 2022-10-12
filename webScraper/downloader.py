from webScraper.models import Collection_Year, Contact_Details, Business, Local_Government, Classification


def get_lga_to_excel(lga: str, year: int):
    data = []

    try:
        year_obj = Collection_Year.objects.filter(year=year)[0]
        lga_obj = Local_Government.objects.filter(local_government_area=lga, year=year_obj)[0]
        businesses = Business.objects.filter(local_government_area=lga_obj)

        return businesses
    except:
        return 1