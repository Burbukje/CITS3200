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
    
    START_CAT_A = '-', ("------------")
    SUPERMARKET = 1.00, ("Supermarket/Grocery Store")
    CONVENIENCE = 2.00, ("Convenience Store")
    WORLDFOOD   = 3.00, ("World/Ethnic Foods")
    HEALTH      = 4.00, ("Health Food Store")
    BUCTHER     = 5.00, ("Butcher/Poultry Store")
    FISHMONGER  = 6.00, ("Fishmonger")
    BAKERY      = 7.00, ("Bakery")
    GREENGROCER = 8.00, ("Fruit and Veg / Greengrocer")
    DELI        = 9.00, ("Delicatessen")
    PATISSERIE  = 10.00, ("Pastry/Patisserie Store")
    CONFECTIONARY = 11.00, ("Confectionary/Chocolate/Ice-Cream")
    OTHER        = 12.00, ("Not otherwise specified")
    LIQUOR      = 13.00, ("Liquor/Bottle Shop")
    GENERAL     = 14.00, ("General Retail")

    START_CAT_B = '--', ("------------")
    CAFE = 15.00, ("Cafe/Coffee shop")

    START_CAT_C = '---', ("------------")

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
    SUPERMARKET = 0.01, ("Supermarket")
    DISCOUNT = 0.02, ("Discount Grocery Store")
    WHOLESALE = 0.03, ("Wholesale Grocery Store")


    @classmethod
    def choices(cls):
        return[(item.value, item.name) for item in cls]


#--------------------------------------------------------------