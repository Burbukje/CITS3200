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
    
def add_statistic_table():
    #year = 2022
    #lga = "ARMADALE, CITY OF"

    query_set = Business.objects.all()

    for business in query_set:
        classification_obj =  Classification.objects.filter(business_id=business)[0]


       # print(classification_obj.classification )
        #print(business.local_government_area)
        newdata= Business_classification(business_name=business.business_name, local_government_area = business.local_government_area,classification = classification_obj.possible_classifications)
        
       # print(newdata.classification)
        newdata.save()
        #print(classification_obj.possible_classifications)
    
    result = Business_classification.objects.values("local_government_area","classification").annotate(dcount=Count("local_government_area")).order_by()
    print(result)

