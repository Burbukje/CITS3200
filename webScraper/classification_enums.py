from winreg import DisableReflectionKey
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
    SUPERMARKET   = 1.00, ("Supermarket/Grocery Store")
    CONVENIENCE   = 2.00, ("Convenience Store")
    WORLDFOOD     = 3.00, ("World/Ethnic Foods")
    HEALTH        = 4.00, ("Health Food Store")
    BUCTHER       = 5.00, ("Butcher/Poultry Store")
    FISHMONGER    = 6.00, ("Fishmonger")
    BAKERY        = 7.00, ("Bakery")
    GREENGROCER   = 8.00, ("Fruit and Veg / Greengrocer")
    DELI          = 9.00, ("Delicatessen")
    PATISSERIE    = 10.00, ("Pastry/Patisserie Store")
    CONFECTIONARY = 11.00, ("Confectionary/Chocolate/Ice-Cream")
    OTHER         = 12.00, ("Not otherwise specified")
    LIQUOR_SHOP   = 13.00, ("Liquor/Bottle Shop")
    GENERAL       = 14.00, ("General Retail")

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

    START_CAT_D      = "-----", ("--- Food Production and Preparation ---")
    HOME_CATERING    = 25.00, ("Home-Based Catering Business/Kitchens or Cooking Classes")
    FOOD_TRUCK       = 26.00, ("Food Truck / Coffee or other Drinks Van")
    DELIVERY_SERVICE = 27.00, ("Meal / Grocery Delivery Service")
    MANUFACTURER    = 28.00, ("Food Manufacturer / Processor")
    PRODUCER        = 29.00, ("Producer / Packer / Distributor")

    START_CAT_E     = "------", ("Institutional Food")
    HOSPITAL        = 30.00, ("Hospitals")
    RESIENTIAL      = 31.00, ("Residential Care")
    DEFENCE         = 32.00, ("Defence")

    START_CAT_F     = "-------", ("Accommodation / Recreation Services")
    HEALTH_LEISURE  = 33.00, ("Health and Leisure Venue")
    ACCOMODATION    = 34.00, ("Accommodatin with Food")

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
    SUP_GROCERY = "-", ("--- Supermarket/Grocery Store ---")
    SUPERMARKET = 0.01, ("Supermarket")
    DISCOUNT = 0.02, ("Discount Grocery Store")
    WHOLESALE = 0.03, ("Wholesale Grocery Store")

    CONVENIENCE = "--", ("--- Convenience Store ---")
    PETROL = 0.04, ("Petrol Station Store")

    @classmethod
    def choices(cls):
        return[(item.value, item.name) for item in cls]


#--------------------------------------------------------------