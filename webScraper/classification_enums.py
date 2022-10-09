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
    OTHER         = 'A12.00', ("Not otherwise specified")
    LIQUOR_SHOP   = 'A13.00', ("Liquor/Bottle Shop")
    GENERAL       = 'A14.00', ("General Retail")

    START_CAT_B   = '---', ("---- Food Service ----")
    RESTAURANT    = 'B01.00', ("Restaurant")
    CAFE          = 'B02.00', ("Cafe/Coffee shop")
    FAST_FOOD     = 'B03.00', ("Fast Casual/Quick Service/Takeaway")
    LIQUOR_VENUE  = 'B04.00', ("Licensed Liquor Venue")
    KIOSK         = 'B05.00', ("Kiosk")
    MOBILE_VENUE  = 'B06.00', ("Mobile food or coffee van/truck venue")
    MARKET_VENUE  = 'B07.00', ("Food Market Venue")

    START_CAT_C   = '----', ("---- Charitable Food Provison ----")
    GROCERIES     = 'C01.00', ("Emergency food provision - groceries")
    MEALS         = 'C02.00', ("Emergency food provision - meals")
    DELIVERY      = 'C03.00', ("Meal preparation and delivery")

    START_CAT_D      = '-----', ("--- Food Production and Preparation ---")
    HOME_CATERING    = 'D01.00', ("Home-Based Catering Business/Kitchens or Cooking Classes")
    FOOD_TRUCK       = 'D02.00', ("Food Truck / Coffee or other Drinks Van")
    DELIVERY_SERVICE = 'D03.00', ("Meal / Grocery Delivery Service")
    MANUFACTURER     = 'D04.00', ("Food Manufacturer / Processor")
    PRODUCER         = 'D05.00', ("Producer / Packer / Distributor")

    START_CAT_E    = '------', ("--- Institutional Food ---")
    HOSPITAL       = 'E01.00', ("Hospitals")
    RESIENTIAL     = 'E02.00', ("Residential Care")
    DEFENCE        = 'E03.00', ("Defence")

    START_CAT_F    = '-------', ("--- Accommodation / Recreation Services ---")
    HEALTH_LEISURE = 'F01.00', ("Health and Leisure Venue")
    ACCOMODATION   = 'F02.00', ("Accommodatin with Food")

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
    SUPERMARKET = 'A1.01', ("Supermarket")
    DISCOUNT    = 'A1.02', ("Discount Grocery Store")
    WHOLESALE   = 'A1.03', ("Wholesale Grocery Store")

    CONVENIENCE = '---', ("--- Convenience Store ---")
    PETROL      = 'A2.01', ("Petrol Station Store")
    CORNER      = 'A2.02', ("Milk Bar / Corner Store")
    OTHER       = 'A2.03', ("Other Convenience Store")

    HEALTH      = '----', ("--- Health Food Store ---")
    WITH_H      = 'A4.01', ("With Shop Front")
    NO_H        = 'A4.02', ("No Shop Front")

    LIQUOR      = '-----', ("--- Liquor Merchant / Bottle Shop ---")
    WITH_L      = 'A13.01', ("With Shop Front")
    NO_L        = 'A13.02', ("No Shop Front")

    RESTAURANT  = '------', ("--- Restaurant ---")
    MODERN      = 'B2.01', ("Modern Austrlia")
    AMERICAN    = 'B2.02', ("American")
    BRITISH     = 'B2.03', ("British")
    CARIBBEAN   = 'B2.04', ("Caribbean")
    CHINESE     = 'B2.05', ("Chinese")
    INDIAN      = 'B2.06', ("Indian")
    ITALIAN     = 'B2.07', ("Italian")
    VIETNAMESE  = 'B2.08', ("Vietnamese")
    THAI        = 'B2.09', ("Thai")
    JAPANESE    = 'B2.10', ("Japanese")
    INDONESIAN  = 'B2.11', ("Indonesian")
    MALAYSIAN   = 'B2.12', ("Malaysian")
    AFRICAN     = 'B2.13', ("African")
    MEXICAN     = 'B2.14', ("Mexican")
    LEBANESE    = 'B2.15', ("Lebanese")
    TURKISH     = 'B2.16', ("Turkish")
    GREEK       = 'B2.17', ("Greek")
    FRENCH      = 'B2.18', ("French")
    MEDITERRANEAN = 'B2.19', ("Mediterranean")
    SPANISH     = 'B2.20', ("Spanish")
    MOROCCAN    = 'B2.21', ("Moroccan")
    NEPALESES   = 'B2.22', ("Nepalese")
    KOREAN      = 'B2.23', ("Korean")
    CANTONESE   = 'B2.24', ("Cantonese")
    FILLIPNO    = 'B2.25', ("Fillipino")
    MIXED_ASIAN_FUSION = 'B2.26', ("Mixed Asian Fusion")
    SINGAPOREAN = 'B2.27', ("Singaporean")
    TAIWANESE   = 'B2.28', ("Taiwanese")
    EGYPTIAN    = 'B2.29', ("Egyptian")
    GERMAN      = 'B2.30', ("German")
    CAMBODIAN   = 'B2.31', ("Cambodian")
    PERSIAN     = 'B2.32', ("Persian")
    MULTI_CUISINE = 'B2.33', ("Multiple Cuisines")
    AFGHAN      = 'B2.34', ("Afgan")
    POLISH      = 'B2.35', ("Polish")
    AUS_GRILL   = 'B2.36', ("Modern Australian - Grill")
    AUS_CAVERY  = 'B2.37', ("Modern Australian - Cavery")
    SOUTH_AMERICAN = 'B2.38', ("South American")
    IRISH       = 'B2.39', ("Irish")
    Polynesian  = 'B2.40', ("Polynesian")

    TAKEAWAY    = "-------", ("--- Fast Causal / Quick Service / Takeaway ---")
    BURGERS     = 'B3.01', ("Burgers")
    ROAST_CHICKEN = 'B3.02', ("Roast / BQQ Chicken")
    FRIED_CHICKEN = 'B3.03', ("Fried Chicken")
    HOT_CHIPS   = 'B3.04', ("Hot Chips")
    PIZZA       = 'B3.05', ("Pizza")
    KEBAB       = 'B3.06', ("Kebab / Gozleme")
    FISH_CHIPS  = 'B3.07', ("Fish and Chips")
    PRETZEL     = 'B3.08', ("Pretzel")
    SUSHI       = 'B3.09', ("Sushi")
    SANDWHICH   = 'B3.10', ("Sandwich")
    SALAD       = 'B3.11', ("Salad")
    PIES        = 'B3.12', ("Pies")
    CAVERY      = 'B3.13', ("Cavery")
    HOTDOG      = 'B3.14', ("Hotdog")
    CAKE        = 'B3.15', ("Cakes / Pastry / Biscuits")
    ICE_CREAM   = 'B3.16', ("Ice-Cream / Frozen Yogurt")
    JUICE       = 'B3.17', ("Juice / Smoothies / Shakes")
    BUBBLE_TEA  = 'B3.18', ("Bubble Tea")
    TACO        = 'B3.19', ("Taco / Burrito / Nacho")
    ASIAN       = 'B3.20', ("Asian / Noodles")
    COFFEE      = 'B3.21', ("Coffee")
    CURRY       = 'B3.22', ("Curry")
    PASTA       = 'B3.23', ("Pasta")
    MULTI_TYPE  = 'B3.24', ("Multiple Food Types")
    WAFFLE      = 'B3.25', ("Waffles / Pancakes / Crepes")
    VEGAN       = 'B3.26', ("Vegan")
    MCDONALDS   = 'B3.27', ("McDonalds")
    KFC         = 'B3.28', ("KFC")
    DOMINOS     = 'B3.29', ("Dominos")
    HUNGRY_JACKS = 'B3.30', ("Hungry Jacks")
    SUBWAY      = 'B3.31', ("Subway")
    RED_ROOSTER = 'B3.32', ("Red Rooster")

    LIQUOR_VENUE = "--------", ("--- Licensed Liquor Venue ---")
    SERVE       = 'B4.01', ("Serves Food")
    NO_SERVE    = 'B4.02', ("No Food Served, only bar snacks")

    MANUFACTURER = "---------", ("--- Charitable Food Provision ---")
    HIGH_RISK   = 'D4.01', ("Manufacturer of high-risk foods")
    MEDIUM_RISK = 'D2.02', ("Manufacturer of medium-risk foods")
    LOW_RISK    = 'D4.03', ("Manufacturer of low-risk foods")
    ALCOHOL     = 'D4.04', ("Alcohol / Beverages")

    P_P_D = "----------", ("--- Producer / Packer / Distributor ---")
    PACKER      = 'D5.01', ("Packer / Storage")
    DISTRIBUTOR = 'D5.02', ("Distributor")
    PRODUCER    = 'D5.03', ("Producer")

    EDUCATION   = "-----------", ("--- Education ----")
    PRIMARY     = 'E6.01', ("Primary School")
    HIGH        = 'E6.02', ("High School")
    TAFE        = 'E6.03', ("TAFE / University")
    KINDY       = 'E6.04', ("Kindergarten to Year 12")
    OTHER_ED    = 'E6.05', ("Other Education")

    HEALTH_VENUE        = "------------", ("--- Sports / Exercise / Play ---")
    SPORTS              = 'F2.01', ("Sports / Exercise / Play")
    MEMBER_BASED_CLUBS  = 'F2.02', ("Member-based clubs")
    OTHER_CLUBS         = 'F2.03', ("Other clubs")

    ACCOMMODATION   = "-------------", ("--- Accommodation ---")
    SERVICE         = 'F3.01', ("Includes Restaurant / Cafe / Room Service")
    FUNCTION        = 'F3.02', ("Function Rooms Only")
    NO_SERVICE      = 'F3.03', ("No Restaurant / Cafe / Room Service")

    @classmethod
    def choices(cls):
        return[(item.value, item.name) for item in cls]


#--------------------------------------------------------------