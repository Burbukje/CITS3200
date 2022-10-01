import pandas as pd
from webScraper.models import *
from django.db import models
from django.db.models import Count


def get_lga_list():
    shire_list = []

    with open("./map/geoJSON/metro_area_lga.txt", "r") as f:
        for line in f:
            shire_list.append(line.strip())

    shire_list

def delete_everything_in_table(class_name):
    class_name.objects.all().delete()




def  db_add_P_class( data) -> None:
    P_Class_statistic.objects.create(local_government_area =data[ 'local_government_area'] ,possible_classifications =data[ 'classification'], P_classification_count =data[ 'dcount'])

def  db_add_P_category( data) -> None:
    P_Category_statistic.objects.create(local_government_area =data[ 'local_government_area'] ,possible_categories =data[ 'classification'], P_categories_count =data[ 'dcount'])



def add_statistic_table():

    query_set = Business.objects.all()

#make sure everytime using it as temporary table is empty 
    delete_everything_in_table(Business_classification)

    #Possible_classification
    for business in query_set:
        classification_obj =  Classification.objects.filter(business_id=business)[0]
        newdata= Business_classification(business_name=business.business_name, local_government_area = business.local_government_area,classification = classification_obj.possible_classifications)
        newdata.save()
    

    results = Business_classification.objects.values("local_government_area","classification").annotate(dcount=Count("local_government_area")).order_by()
    delete_everything_in_table(P_Class_statistic)
    for count in results:
        db_add_P_class(count)



    #Possible_category
    for business in query_set:
        classification_obj =  Classification.objects.filter(business_id=business)[0]
        newdata= Business_classification(business_name=business.business_name, local_government_area = business.local_government_area,classification = classification_obj.possible_categories )
        newdata.save()

    results = Business_classification.objects.values("local_government_area","classification").annotate(dcount=Count("local_government_area")).order_by()
    delete_everything_in_table(P_Category_statistic)
    for count in results:
        db_add_P_category(count)

   






