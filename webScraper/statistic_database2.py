import pandas as pd
from webScraper.models import *
from django.db import models
from django.db.models import Count
from django.db.models import Sum

category_list = [
    'Supermarket/grocery store',
    'Convenience store',
    'World/ethnic food store',
    'Health food store',
    'Butcher/poultry store',
    'Fishmonger',
    'Bakery',
    'Fruit and vegetable store/greengrocer',
    'Delicatessen',
    'Cake or pastry shop/patisserie',
    'Confectionery/chocolate/ice -cream',
    'Other specialist food outlet',
    'Liquor merchant/bottle shop',
    'General retail',
    'Café/coffee shop',
    'Restaurant',
    'Fast casual/quick service/takeaway',
    'Licensed liquor venue',
    'Kiosk',
    'Mobile food or coffee van/truck venue',
    'Food market venue',
    'Emergency food provision - groceries',
    'Emergency food provision - meals',
    'Meal preparation and delivery',
    'Home-based catering business/kitchens or cooking classes',
    'Food truck/coffee or other drinks van',
    'Meal/grocery delivery service',
    'Food manufacturer/processor',
    'Producer/packer/ distributor',
    'Hospitals',
    'Residential care',
    'Defence',
    'Correctional',
    'Corporate workplace',
    'Education',
    'Childcare',
    'Community/church/hall/ function centre',
    'Residential worksite',
    'Other institutional', 
    'Entertainment venue',
    'Health and leisure venue',
    'Accommodation with food' 
    
    ]


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
            category_count_list = []
            lga_object = Local_Government.objects.filter(local_government_area=lga , year=year_obj.year)[0]
            Businesses  = Business.objects.filter(local_government_area=lga_object)

            
            for business in Businesses:
                class_list.append(Classification.objects.filter(business_id =business)[0].possible_classifications)
                category_count_list.append(Classification.objects.filter(business_id =business)[0].possible_categories)
                

  
            lga_object.food_retail =class_list.count('A-Food Retail')
            lga_object.food_service=class_list.count('B-Food Service')
            lga_object.CHARITABLE_FOOD_PROVISION=class_list.count('C-Charitable_Food_Provision')
            lga_object.FOOD_PRODUCTION_AND_PREPARATION=class_list.count('D-Food Production and Preparation')
            lga_object.INSTITUTIONAL_FOOD=class_list.count('E-Institutional Food')
            lga_object.ACCOMMODATION_RECREATION_SERVICES=class_list.count('F-Accommodation/Recreation Services')

            lga_object.Supermarket_grocery_store=category_count_list.count(category_list[0])
            lga_object.Convenience_store= category_count_list.count(category_list[1])
            lga_object.World_ethnic_food_store= category_count_list.count(category_list[2])
            lga_object.Health_food_store= category_count_list.count(category_list[3])
            lga_object.Butcher_poultry_store= category_count_list.count(category_list[4])
            lga_object.Fishmonger= category_count_list.count(category_list[5])
            lga_object.Bakery= category_count_list.count(category_list[6])
            lga_object.Fruit_and_vegetable_store_greengrocer =category_count_list.count(category_list[7])
            lga_object.Delicatessen= category_count_list.count(category_list[8])
            lga_object.Cake_or_pastry_shop_patisserie= category_count_list.count(category_list[9])
            lga_object.Confectionery_chocolate_icecream = category_count_list.count(category_list[10])
            lga_object.Other_specialist_food_outlet= category_count_list.count(category_list[11])
            lga_object.Liquor_merchant_bottle_shop= category_count_list.count(category_list[12])
            lga_object.General_retail= category_count_list.count(category_list[13])
            lga_object.Café_coffee_shop= category_count_list.count(category_list[14])
            lga_object.Restaurant= category_count_list.count(category_list[15])
            lga_object.Fast_casual_quick_service_takeaway= category_count_list.count(category_list[16])
            lga_object.Licensed_liquor_venue= category_count_list.count(category_list[17])
            lga_object.Kiosk= category_count_list.count(category_list[18])
            lga_object.Mobile_food_or_coffee_van_truck_venue= category_count_list.count(category_list[19])
            lga_object.Food_market_venue= category_count_list.count(category_list[20])
            lga_object.Emergency_food_provision_groceries= category_count_list.count(category_list[21])
            lga_object.Emergency_food_provision_meals= category_count_list.count(category_list[22])
            lga_object.Meal_preparation_and_delivery= category_count_list.count(category_list[23])
            lga_object.Home_based_catering_business_kitchens_or_cooking_classes= category_count_list.count(category_list[24])
            lga_object.Food_truck_coffee_or_other_drinks_van= category_count_list.count(category_list[25])
            lga_object.Meal_grocery_delivery_service= category_count_list.count(category_list[26])
            lga_object.Food_manufacturer_processor= category_count_list.count(category_list[27])
            lga_object.Producer_packer_distributor= category_count_list.count(category_list[28])
            lga_object.Hospitals= category_count_list.count(category_list[29])
            lga_object.Residential_care= category_count_list.count(category_list[30])
            lga_object.Defence= category_count_list.count(category_list[31])
            lga_object.Correctional= category_count_list.count(category_list[32])
            lga_object.Corporate_workplace= category_count_list.count(category_list[33])
            lga_object.Education= category_count_list.count(category_list[34])
            lga_object.Childcare= category_count_list.count(category_list[35])
            lga_object.Community_church_hall_function_centre= category_count_list.count(category_list[36])
            lga_object.Residential_worksite= category_count_list.count(category_list[37])
            lga_object.Other_institutional=category_count_list.count(category_list[38])
            lga_object.Entertainment_venue= category_count_list.count(category_list[39])
            lga_object.Health_and_leisure_venue= category_count_list.count(category_list[40])
            lga_object.Accommodation_with_food= category_count_list.count(category_list[41])


            lga_object.save()







        
       