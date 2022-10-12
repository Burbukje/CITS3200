from webScraper.models import Collection_Year, Contact_Details, Business, Local_Government, Classification
import pandas as pd
from django.db.models import Count
import geopandas as gpd


GB_TYPES = "webScraper/static/assets/GOOGLE API BUSSINESS TYPE NAMES.xlsx"



#import classification matching spreadsheet 
def get_match_sheet():
    match_sheet = pd.read_excel(GB_TYPES,header=0,sheet_name = 'Only_matched')
    match_sheet['GOOGLE API ALL BUSINESS TYPE'] = match_sheet['GOOGLE API ALL BUSINESS TYPE'].str.strip()
    match_sheet['GOOGLE API ALL BUSINESS TYPE'] = match_sheet['GOOGLE API ALL BUSINESS TYPE'].str.lower()

    return match_sheet


#import all Local government area title as a list
def get_lga_list():
    lga_list = []
    boundary_geojson = gpd.read_file('map/geoJSON/LGA_Boundaries_Metro_Area.geojson')
    for lga in boundary_geojson['name']:
        lga_list.append(lga)
    return lga_list



#convert the classification spreadsheet to dictionary
def classification_dictionarys(match_sheet):
    match_sheet['Weight'] = match_sheet['Weight'].astype(int)
    classification  = dict(zip(match_sheet['GOOGLE API ALL BUSINESS TYPE'], match_sheet['Classification']))
    Category  = dict(zip(match_sheet['GOOGLE API ALL BUSINESS TYPE'], match_sheet['Category']))
    Category_code  = dict(zip(match_sheet['GOOGLE API ALL BUSINESS TYPE'], match_sheet['Category code']))
    Sub_category  = dict(zip(match_sheet['GOOGLE API ALL BUSINESS TYPE'], match_sheet['Sub-category']))
    Sub_category_code  = dict(zip(match_sheet['GOOGLE API ALL BUSINESS TYPE'], match_sheet['Sub- category code']))

    classification  = {a : (c, b) for (a, b), c in zip(classification.items(), match_sheet['Weight'])} 
    Category  = {a : (c, b) for (a, b), c in zip(Category.items(),match_sheet['Weight'])} 
    Category_code  = {a : (c, b) for (a, b), c in zip(Category_code.items(),match_sheet['Weight'])} 
    Sub_category  = {a : (c, b) for (a, b), c in zip(Sub_category.items(), match_sheet['Weight'])} 
    Sub_category_code  = {a : (c, b)for (a, b), c in zip(Sub_category_code.items(), match_sheet['Weight'])} 
  
    return classification,Category,Category_code,Sub_category,Sub_category_code


#match the google business_type by the classification dictionary 
def class_matching(business_type_list,classification,Category,Category_code,Sub_category,Sub_category_code):

    #classification,Category,Category_code,Sub_category,Sub_category_code = classification_dictionarys(match_sheet)

    classification_l = []
    Category_l = []
    Category_code_l = []
    Sub_category_l = []
    Sub_category_code_l = []
    
    try:
      
        type_list = eval(business_type_list)

    except:
        type_list = ['undefined']



    for key in type_list:
        key =  key.strip()
        classification_l.append(classification.get(key,(0,'undefined')))
        Category_l.append(Category.get(key.strip(),(0,'undefined')))
        Category_code_l.append(Category_code.get(key.strip(),(0,'undefined')))
        Sub_category_l.append(Sub_category.get(key.strip(),(0,'undefined')))
        Sub_category_code_l.append(Sub_category_code.get(key.strip(),(0,'undefined'))) 





    #remove na
    classification_l =[x for x in classification_l if x == x]
    Category_l = [x for x in  Category_l if x == x]
    Category_code_l = [x for x in Category_code_l if x == x]
    Sub_category_l = [x for x in Sub_category_l if x == x]
    Sub_category_code_l = [x for x in Sub_category_code_l if x == x]


    #get maximum
    classification_l =max(classification_l,key=lambda item:item[0], default=[(0,'undefined')])
    Category_l = max(Category_l,key=lambda item:item[0], default=[(0,'undefined')])
    Category_code_l =max(Category_code_l,key=lambda item:item[0], default=[(0,'undefined')])
    Sub_category_l = max(Sub_category_l,key=lambda item:item[0], default=[(0,'undefined')])
    Sub_category_code_l = max(Sub_category_code_l ,key=lambda item:item[0], default=[(0,'undefined')])

    #remove duplicate
    classification_l =list(dict.fromkeys(classification_l))
    Category_l = list(dict.fromkeys(Category_l))
    Category_code_l = list(dict.fromkeys(Category_code_l))
    Sub_category_l = list(dict.fromkeys(Sub_category_l ))
    Sub_category_code_l = list(dict.fromkeys(Sub_category_code_l))
   
    #return a result as a dictionary containing all matched calssifciation
    result = {
     'classification':   [classification_l[1], 'code'],
     'category_one':     [Category_l[1], Category_code_l[1]],
     'sub_category_one': [Sub_category_l[1],Sub_category_code_l[1]]}
   
    return result

def  db_add_possible_classification( classification_obj, matched) -> None:

    classification_name = matched


    classification_obj.possible_classifications = classification_name

   #print(classification_obj)
    classification_obj.save()


def  db_add_possible_cats(classification, matched) -> None:

    categories_name = matched
    classification.possible_categories = categories_name
    classification.save()




###################################### Combine all function 

def get_lga_business():


    #add the years you want to update
    years = [2022] 


    #update choosen LGA or ALL (all - get_lga_list())
   # lga_list = ["ARMADALE, CITY OF","EAST FREMANTLE, TOWN OF"]
    lga_list =  get_lga_list()





    match_sheet = get_match_sheet()
    classification,Category,Category_code,Sub_category,Sub_category_code = classification_dictionarys(match_sheet) 



    for year in years:
        for lga in lga_list:
            print(lga)

            year_obj = Collection_Year.objects.filter(year=year)[0]
            lga_object = Local_Government.objects.filter(local_government_area=lga, year=year_obj)
            

            if lga_object:
                print(lga_object)
                query_set = Business.objects.filter(local_government_area=lga_object[0])


                for business in query_set:
                    classification_obj = Classification.objects.filter(business_id=business)
    
                    print(business.google_business_types)

    
                    matched = class_matching(business.google_business_types,classification,Category,Category_code,Sub_category,Sub_category_code)
                    db_add_possible_classification(classification_obj[0], matched['classification'][0])
                    db_add_possible_cats(classification_obj[0], matched['category_one'][0])