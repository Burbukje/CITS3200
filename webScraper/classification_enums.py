from django.db import models

class Classification_Appendix(models.TextChoices):
    DEFAULT = '-', ("------------")
    A = 'A', ("Food Retail")
    B = 'B', ("Food Service")
    C = 'C', ("Charitable Food Provisions")
    D = 'D', ("Food Productiond and Preperation")
    E = 'E', ("Institutional Food") 
    F = 'F', ("Accomadation and Recreation")

    @classmethod
    def choices(cls):
        return[(item.value, item.name) for item in cls]


#---------------NOT USED-------------------------
class Category_A(models.TextChoices):
    DEFAULT       = '-', ("------------")

    START_CAT_A   = '--', ("---- Food Retail ----")
    SUPERMARKET   = 'A1.00', ("Supermarket/Grocery Store")
    CONVENIENCE   = 'A2.00', ("Convenience Store")
    WORLDFOOD     = 'A3.00', ("World/Ethnic Foods")
    HEALTH        = 'A4.00', ("Health Food Store")
    BUCTHER       = 'A5.00', ("Butcher/Poultry Store")
    FISHMONGER    = 'A6.00', ("Fishmonger")
    BAKERY        = 'A7.00', ("Bakery")
    GREENGROCER   = 'A8.00', ("Fruit and Veg / Greengrocer")
    DELI          = 'A9.00', ("Delicatessen")
    PATISSERIE    = 'A10.00', ("Pastry/Patisserie Store")
    CONFECTIONARY = 'A11.00', ("Confectionary/Chocolate/Ice-Cream")
    OTHER         = 'A12.0', ("Not otherwise specified")
    LIQUOR_SHOP   = 'A13.0', ("Liquor/Bottle Shop")
    GENERAL       = 'A14.0', ("General Retail")

    START_CAT_B   = '---', ("---- Food Service ----")
    CAFE          = 15.00, ("Cafe/Coffee shop")
    RESTAURANT    = 16.00, ("Restaurant")
    FAST_FOOD     = 17.00, ("Fast Casual/Quick Service/Takeaway")
    LIQUOR_VENUE  = 18.00, ("Licensed Liquor Venue")
    KIOSK         = 19.00, ("Kiosk")
    MOBILE_VENUE  = 20.00, ("Mobile food or coffee van/truck venue")
    MARKET_VENUE  = 21.00, ("Food Market Venue")

    START_CAT_C   = '----', ("---- Charitable Food Provison ----")
    GROCERIES     = 22.00, ("Emergency food provision - groceries")
    MEALS         = 23.00, ("Emergency food provision - meals")
    DELIVERY      = 24.00, ("Meal preparation and delivery")

    START_CAT_D      = '-----', ("--- Food Production and Preparation ---")
    HOME_CATERING    = 25.00, ("Home-Based Catering Business/Kitchens or Cooking Classes")
    FOOD_TRUCK       = 26.00, ("Food Truck / Coffee or other Drinks Van")
    DELIVERY_SERVICE = 27.00, ("Meal / Grocery Delivery Service")
    MANUFACTURER     = 28.00, ("Food Manufacturer / Processor")
    PRODUCER         = 29.00, ("Producer / Packer / Distributor")

    START_CAT_E    = '------', ("--- Institutional Food ---")
    HOSPITAL       = 30.00, ("Hospitals")
    RESIENTIAL     = 31.00, ("Residential Care")
    DEFENCE        = 32.00, ("Defence")

    START_CAT_F    = '-------', ("--- Accommodation / Recreation Services ---")
    HEALTH_LEISURE = 33.00, ("Health and Leisure Venue")
    ACCOMODATION   = 34.00, ("Accommodatin with Food")

    @classmethod
    def choices(cls):
        return[(item.value, item.name) for item in cls]


class Category_B(models.TextChoices):

    @classmethod
    def choices(cls):
        return[(item.value, item.name) for item in cls]


class Category_C(models.TextChoices):

    
    @classmethod
    def choices(cls):
        return[(item.value, item.name) for item in cls]


class Category_D(models.TextChoices):

    
    @classmethod
    def choices(cls):
        return[(item.value, item.name) for item in cls]


class Category_E(models.TextChoices):

    
    @classmethod
    def choices(cls):
        return[(item.value, item.name) for item in cls]


class Category_F(models.TextChoices):

    
    @classmethod
    def choices(cls):
        return[(item.value, item.name) for item in cls]


class Sub_Category_One(models.TextChoices):
    DEFAULT = '-', ("------------")

    SUP_GROCERY = '--', ("--- Supermarket/Grocery Store ---")
    SUPERMARKET = 0.01, ("Supermarket")
    DISCOUNT    = 0.02, ("Discount Grocery Store")
    WHOLESALE   = 0.03, ("Wholesale Grocery Store")

    CONVENIENCE = '---', ("--- Convenience Store ---")
    PETROL      = 0.04, ("Petrol Station Store")
    CORNER      = 0.05, ("Milk Bar / Corner Store")
    OTHER       = 0.06, ("Other Convenience Store")

    HEALTH      = '----', ("--- Health Food Store ---")
    WITH_H      = 0.07, ("With Shop Front")
    NO_H        = 0.08, ("No Shop Front")

    LIQUOR      = '-----', ("--- Liquor Merchant / Bottle Shop ---")
    WITH_L      = 0.09, ("With Shop Front")
    NO_L        = 0.10, ("No Shop Front")

    RESTAURANT  = '------', ("--- Restaurant ---")
    MODERN      = 0.11, ("Modern Austrlia")
    AMERICAN    = 0.12, ("American")
    BRITISH     = 0.13, ("British")
    CARIBBEAN   = 0.14, ("Caribbean")
    CHINESE     = 0.15, ("Chinese")
    INDIAN      = 0.16, ("Indian")
    ITALIAN     = 0.17, ("Italian")
    VIETNAMESE  = 0.18, ("Vietnamese")
    THAI        = 0.19, ("Thai")
    JAPANESE    = 0.20, ("Japanese")
    INDONESIAN  = 0.21, ("Indonesian")
    MALAYSIAN   = 0.22, ("Malaysian")
    AFRICAN     = 0.23, ("African")
    MEXICAN     = 0.24, ("Mexican")
    LEBANESE    = 0.25, ("Lebanese")
    TURKISH     = 0.26, ("Turkish")
    GREEK       = 0.27, ("Greek")
    FRENCH      = 0.28, ("French")
    MEDITERRANEAN = 0.29, ("Mediterranean")
    SPANISH     = 0.30, ("Spanish")
    MOROCCAN    = 0.31, ("Moroccan")
    NEPALESES   = 0.32, ("Nepalese")
    KOREAN      = 0.33, ("Korean")
    CANTONESE   = 0.34, ("Cantonese")
    FILLIPNO    = 0.35, ("Fillipino")
    MIXED_ASIAN_FUSION = 0.36, ("Mixed Asian Fusion")
    SINGAPOREAN = 0.37, ("Singaporean")
    TAIWANESE   = 0.38, ("Taiwanese")
    EGYPTIAN    = 0.39, ("Egyptian")
    GERMAN      = 0.40, ("German")
    CAMBODIAN   = 0.41, ("Cambodian")
    PERSIAN     = 0.42, ("Persian")
    MULTI_CUISINE = 0.43, ("Multiple Cuisines")
    AFGHAN      = 0.44, ("Afgan")
    POLISH      = 0.45, ("Polish")
    AUS_GRILL   = 0.46, ("Modern Australian - Grill")
    AUS_CAVERY  = 0.47, ("Modern Australian - Cavery")
    SOUTH_AMERICAN = 0.48, ("South American")
    IRISH       = 0.49, ("Irish")
    Polynesian  = 0.50, ("Polynesian")

    TAKEAWAY    = "-------", ("--- Fast Causal / Quick Service / Takeaway ---")
    BURGERS     = 0.51, ("Burgers")
    ROAST_CHICKEN = 0.52, ("Roast / BQQ Chicken")
    FRIED_CHICKEN = 0.53, ("Fried Chicken")
    HOT_CHIPS   = 0.54, ("Hot Chips")
    PIZZA       = 0.55, ("Pizza")
    KEBAB       = 0.56, ("Kebab / Gozleme")
    FISH_CHIPS  = 0.57, ("Fish and Chips")
    PRETZEL     = 0.58, ("Pretzel")
    SUSHI       = 0.59, ("Sushi")
    SANDWHICH   = 0.60, ("Sandwich")
    SALAD       = 0.61, ("Salad")
    PIES        = 0.62, ("Pies")
    CAVERY      = 0.63, ("Cavery")
    HOTDOG      = 0.64, ("Hotdog")
    CAKE        = 0.65, ("Cakes / Pastry / Biscuits")
    ICE_CREAM   = 0.66, ("Ice-Cream / Frozen Yogurt")
    JUICE       = 0.67, ("Juice / Smoothies / Shakes")
    BUBBLE_TEA  = 0.68, ("Bubble Tea")
    TACO        = 0.69, ("Taco / Burrito / Nacho")
    ASIAN       = 0.70, ("Asian / Noodles")
    COFFEE      = 0.71, ("Coffee")
    CURRY       = 0.72, ("Curry")
    PASTA       = 0.73, ("Pasta")
    MULTI_TYPE  = 0.74, ("Multiple Food Types")
    WAFFLE      = 0.75, ("Waffles / Pancakes / Crepes")
    VEGAN       = 0.76, ("Vegan")
    MCDONALDS   = 0.77, ("McDonalds")
    KFC         = 0.78, ("KFC")
    DOMINOS     = 0.79, ("Dominos")
    HUNGRY_JACKS = 0.80, ("Hungry Jacks")
    SUBWAY      = 0.81, ("Subway")
    RED_ROOSTER = 0.82, ("Red Rooster")

    LIQUOR_VENUE = "--------", ("--- Licensed Liquor Venue ---")
    SERVE       = 0.83, ("Serves Food")
    NO_SERVE    = 0.84, ("No Food Served, only bar snacks")

    MANUFACTURER = "---------", ("--- Charitable Food Provision ---")
    HIGH_RISK   = 0.85, ("Manufacturer of high-risk foods")
    MEDIUM_RISK = 0.86, ("Manufacturer of medium-risk foods")
    LOW_RISK    = 0.87, ("Manufacturer of low-risk foods")
    ALCOHOL     = 0.88, ("Alcohol / Beverages")

    P_P_D = "----------", ("--- Producer / Packer / Distributor ---")
    PACKER      = 0.89, ("Packer / Storage")
    DISTRIBUTOR = 0.90, ("Distributor")
    PRODUCER    = 0.91, ("Producer")

    EDUCATION   = "-----------", ("--- Education ----")
    PRIMARY     = 0.92, ("Primary School")
    HIGH        = 0.93, ("High School")
    TAFE        = 0.94, ("TAFE / University")
    KINDY       = 0.95, ("Kindergarten to Year 12")
    OTHER_ED    = 0.96, ("Other Education")

    HEALTH_VENUE        = "------------", ("--- Sports / Exercise / Play ---")
    SPORTS              = 0.97, ("Sports / Exercise / Play")
    MEMBER_BASED_CLUBS  = 0.98, ("Member-based clubs")
    OTHER_CLUBS         = 0.99, ("Other clubs")

    ACCOMMODATION   = "-------------", ("--- Accommodation ---")
    SERVICE         = 1.00, ("Includes Restaurant / Cafe / Room Service")
    FUNCTION        = 1.01, ("Function Rooms Only")
    NO_SERVICE      = 1.02, ("No Restaurant / Cafe / Room Service")

    @classmethod
    def choices(cls):
        return[(item.value, item.name) for item in cls]


#--------------------------------------------------------------