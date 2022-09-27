from webScraper.models import Collection_Year, Contact_Details, Business, Local_Government, Classification
import pandas as pd
GB_TYPES = "webScraper/static/assets/GOOGLE_API_BUSSINESS_TYPE_NAMES.xlsx"



def  db_add_possible_classification(classification, matched) -> None:

    classification_name = matched
    classification.possible_classifications = classification_name
    classification.save()


def  db_add_possible_cats(classification, matched) -> None:

    categories_name = matched
    classification.possible_categories = categories_name
    classification.save()


def get_match_sheet():
    match_sheet = pd.read_excel(GB_TYPES,header=0,sheet_name = 'Only_matched')
    match_sheet['GOOGLE API ALL BUSINESS TYPE'] = match_sheet['GOOGLE API ALL BUSINESS TYPE'].str.strip()
    match_sheet['GOOGLE API ALL BUSINESS TYPE'] = match_sheet['GOOGLE API ALL BUSINESS TYPE'].str.lower()

    return match_sheet


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


def class_matching(business_type_list,match_sheet):

    classification,Category,Category_code,Sub_category,Sub_category_code = classification_dictionarys(match_sheet)
  
    classification_l = []
    Category_l = []
    Category_code_l = []
    Sub_category_l = []
    Sub_category_code_l = []

    for business_obj in business_type_list:
        
        google_types = business_obj.google_business_types
        classification_obj = Classification.objects.filter(business_id=business_obj)[0]

        db_add_possible_classification(classification_obj, "THIS IS A TEST")

        print(google_types)
        break

        # classification_l.append(classification.get(key,(0,'undefined')))
        # Category_l.append(Category.get(key.strip(),(0,'undefined')))
        # Category_code_l.append(Category_code.get(key.strip(),(0,'undefined')))
        # Sub_category_l.append(Sub_category.get(key.strip(),(0,'undefined')))
        # Sub_category_code_l.append(Sub_category_code.get(key.strip(),(0,'undefined'))) 

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
   
    result = {
     'classification':   [classification_l[1], 'code'],
     'category_one':     [Category_l[1], Category_code_l[1]],
     'sub_category_one': [Sub_category_l[1],Sub_category_code_l[1]]}
   
    return result


def get_lga_business():
    # year = int(year)
    # lga = lga.upper()

    year = 2022
    lga = "ARMADALE, CITY OF"

    year_obj = Collection_Year.objects.filter(year=year)[0]
    lga_object = Local_Government.objects.filter(local_government_area=lga, year=year_obj)[0]
    query_set = Business.objects.filter(local_government_area=lga_object)

    class_matching(query_set, get_match_sheet())



