import pandas as pd
from webScraper.models import *
from django.db import models
from django.db.models import Count
from django.db.models import Sum



def get_lga_list():
    shire_list = []

    with open("map/geoJSON/metro_area_lga.txt", "r") as f:
        for line in f:
            shire_list.append(line.strip())

    return shire_list


def add_statistic_table():
    year_list = [2022]
    lga_list = get_lga_list()



    
    for year in year_list:
        year_obj = Collection_Year.objects.filter(year=year)[0]
        
        for lga in lga_list:
            class_list = []
            lga_object = Local_Government.objects.filter(local_government_area=lga , year=year_obj.year)[0]
            Businesses  = Business.objects.filter(local_government_area=lga_object)

            
            for business in Businesses:
                class_list.append(Classification.objects.filter(business_id =business)[0].possible_classifications)



            lga_object.food_retail =class_list.count('A-Food Retail')
            lga_object.food_service=class_list.count('B-Food Service')
            lga_object.CHARITABLE_FOOD_PROVISION=class_list.count('C-Charitable_Fiid_Provision')
            lga_object.FOOD_PRODUCTION_AND_PREPARATION=class_list.count('D-Food Production and Preparation')
            lga_object.INSTITUTIONAL_FOOD=class_list.count('E-Institutional Food')
            lga_object.ACCOMMODATION_RECREATION_SERVICES=class_list.count('F-Accommodation/Recreation Services')

            lga_object.save()







        
       