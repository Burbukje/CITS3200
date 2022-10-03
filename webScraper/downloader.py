from webScraper.models import Collection_Year, Contact_Details, Business, Local_Government, Classification


def get_lga_to_excel(lga: str, year: int):
    data = []

    year = Collection_Year.objects.filter(year=year)
    lga = Local_Government.objects.filter(local_government_area=lga)
    



    return data