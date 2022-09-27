from webScraper.models import Collection_Year, Contact_Details, Business, Local_Government, Classification


def  db_add_possible_classification(classification, headers: list,matched) -> None:

    classification_name = matched
    classification.possible_classifications = classification_name
    classification.save()

def get_match_sheet():
    match_sheet = pd.read_excel('GOOGLE API BUSSINESS TYPE NAMES.xlsx',header=0,sheet_name = 'Only_matched')
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


def class_matching(business_type_list,match_sheet) :

    classification,Category,Category_code,Sub_category,Sub_category_code = classification_dictionarys(match_sheet)
  
    classification_l = []
    Category_l = []
    Category_code_l = []
    Sub_category_l = []
    Sub_category_code_l = []

    for k in business_type_list :
        key = k.strip()
        classification_l.append(classification.get(key,(0,'undefined')))
        Category_l.append(Category.get(key.strip(),(0,'undefined')))
        Category_code_l.append(Category_code.get(key.strip(),(0,'undefined')))
        Sub_category_l.append(Sub_category.get(key.strip(),(0,'undefined')))
        Sub_category_code_l.append(Sub_category_code.get(key.strip(),(0,'undefined'))
) 

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


