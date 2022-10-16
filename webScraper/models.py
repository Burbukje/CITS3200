from django.db import models
import uuid
from webScraper.classification_enums import *
import json

# Create your models here.


#------------------------------------Business DB--------------------------------------------


class Collection_Year(models.Model):
    year = models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.year)

    def get_year(self) -> int:
        return self.year


class Local_Government(models.Model):
    year = models.ForeignKey(Collection_Year, on_delete=models.CASCADE)
    local_government_area = models.CharField(max_length=128)
    # classifications = models.ForeignKey(P_Class, on_delete=models.CASCADE)
    
    food_retail = models.IntegerField(default=0)
    food_service = models.IntegerField(default=0)
    CHARITABLE_FOOD_PROVISION = models.IntegerField(default=0)
    FOOD_PRODUCTION_AND_PREPARATION = models.IntegerField(default=0)
    INSTITUTIONAL_FOOD = models.IntegerField(default=0)
    ACCOMMODATION_RECREATION_SERVICES = models.IntegerField(default=0)

    Supermarket_grocery_store= models.IntegerField(default=0)
    Convenience_store= models.IntegerField(default=0)
    World_ethnic_food_store= models.IntegerField(default=0)
    Health_food_store= models.IntegerField(default=0)
    Butcher_poultry_store= models.IntegerField(default=0)
    Fishmonger= models.IntegerField(default=0)
    Bakery= models.IntegerField(default=0)
    Fruit_and_vegetable_store_greengrocer = models.IntegerField(default=0)
    Delicatessen= models.IntegerField(default=0)
    Cake_or_pastry_shop_patisserie= models.IntegerField(default=0)
    Confectionery_chocolate_icecream = models.IntegerField(default=0)
    Other_specialist_food_outlet= models.IntegerField(default=0)
    Liquor_merchant_bottle_shop= models.IntegerField(default=0)
    business_as_secondary_classification= models.IntegerField(default=0)
    General_retail= models.IntegerField(default=0)
    Café_coffee_shop= models.IntegerField(default=0)
    Restaurant= models.IntegerField(default=0)
    Fast_casual_quick_service_takeaway= models.IntegerField(default=0)
    Licensed_liquor_venue= models.IntegerField(default=0)
    Kiosk= models.IntegerField(default=0)
    Mobile_food_or_coffee_van_truck_venue= models.IntegerField(default=0)
    Food_market_venue= models.IntegerField(default=0)
    Emergency_food_provision_groceries= models.IntegerField(default=0)
    Emergency_food_provision_meals= models.IntegerField(default=0)
    Meal_preparation_and_delivery= models.IntegerField(default=0)
    Home_based_catering_business_kitchens_or_cooking_classes= models.IntegerField(default=0)
    Food_truck_coffee_or_other_drinks_van= models.IntegerField(default=0)
    Meal_grocery_delivery_service= models.IntegerField(default=0)
    Food_manufacturer_processor= models.IntegerField(default=0)
    Producer_packer_distributor= models.IntegerField(default=0)
    Hospitals= models.IntegerField(default=0)
    Residential_care= models.IntegerField(default=0)
    Defence= models.IntegerField(default=0)
    Correctional= models.IntegerField(default=0)
    Corporate_workplace= models.IntegerField(default=0)
    Education= models.IntegerField(default=0)
    Childcare= models.IntegerField(default=0)
    Community_church_hall_function_centre= models.IntegerField(default=0)
    Residential_worksite= models.IntegerField(default=0)
    Other_institutional= models.IntegerField(default=0)
    Entertainment_venue= models.IntegerField(default=0)
    Health_and_leisure_venue= models.IntegerField(default=0)
    Accommodation_with_food= models.IntegerField(default=0)

    def __str__(self):
        return f'{self.get_year()}-{self.local_government_area}'

    def get_year(self) -> int:
        return self.year.get_year()

    def get_lga(self) -> str:
        return self.local_government_area


class Business(models.Model):
    local_government_area = models.ForeignKey(Local_Government, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business_name = models.CharField(max_length=128)
    google_id = models.CharField(max_length=128, null=True, default=" ")
    google_business_types = models.CharField(max_length=128, null=True, default=" ")
    notes = models.TextField(max_length=256, null=True)

    def __str__(self):
        lga = self.local_government_area.get_lga()
        year = self.local_government_area.get_year()
        return f'{year}-{self.business_name} ({lga})'

    def get_name(self) -> str:
        return self.business_name

    def get_notes(self) -> str:
        return self.notes

    def get_id(self):
        return self.id

    def get_google_id(self):
        return self.google_id

class Contact_Details(models.Model):
    business_id = models.OneToOneField(Business, null=True, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, default=-31.9524993)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, default=115.8612164)
    parcel_address = models.CharField(max_length=128, null=True, default="")
    formatted_address = models.CharField(max_length=128, null=True, default="")
    phone = models.CharField(max_length=15, null=True, default="")
    phone_mobile = models.CharField(max_length=15, null=True, default="")
    website = models.CharField(max_length=128, null=True, default="")
    email = models.CharField(max_length=128, null=True, default="")
    menu = models.BooleanField(default=False, null=True)
    opening_hours = models.JSONField(default=[' '], null=True)

    def __str__(self):
        year = self.business_id.local_government_area.get_year()
        return f'{year}-{self.business_id.get_name()} (Phone: {self.get_phone()} Website: {self.get_website()})'

    def get_name(self) -> str:
        return str(self.business_id.get_name())

    def get_lat(self) -> int:
        return self.latitude

    def get_long(self):
        return self.longitude

    def get_parcel_add(self):
        return self.parcel_address

    def get_formatted_add(self):
        return self.formatted_address

    def get_phone(self):
        if self.phone == '':
            return 'None'
        return self.phone
    
    def get_website(self):
        if self.website == '':
            return 'None'
        return self.website

    def get_email(self):
        return self.email

    def get_menu(self):
        return self.menu

    def get_opening(self):
        return json.dumps(self.opening_hours)


class Classification(models.Model):
    business_id = models.OneToOneField(Business, null=True, on_delete=models.CASCADE)
    possible_classifications = models.CharField(max_length=128, null=True, default="None")
    classification = models.CharField(max_length=1, choices=Classification_Appendix.choices, null=True, default="None")
    possible_categories = models.CharField(max_length=128, null=True, default="None")
    category_one = models.CharField(max_length=16, choices=Category_A.choices, null=True, default="None")
    sub_cat_one = models.CharField(max_length=16, choices = Sub_Category_One.choices, null=True, default="None")

    # category_two = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    # sub_cat_two = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    # category_three = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    # sub_cat_three = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    def __str__(self):
        year = self.business_id.local_government_area.get_year()
        return f'{year}-{self.business_id.get_name()} (Class: {self.classification} Category: {self.category_one})'

    def get_class(self) -> str:
        return self.possible_classifications
        
    def get_cat_one(self) -> str:
        return self.possible_categories

    def get_sub_cat_one(self) -> str:
        return self.sub_cat_one

    # def get_cat_two(self) -> int:
    #     return self.category_two

    # def get_sub_cat_two(self) -> int:
    #     return self.sub_cat_two

    # def get_cat_three(self) -> int:
    #     return self.category_three

    # def get_sub_cat_three(self) -> int:
    #     return self.sub_cat_three


#---------------------------------User Login------------------------------------------

from datetime import date

from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class DecadeBornListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Local Government Areas')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'LGA'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('ARMADALE', _('ARMADALE, CITY OF')),
            ('90s', _('in the nineties')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == 'ARMADALE':
            return queryset.filter(
                local_government='ARMADALE, CITY OF'
            )
        if self.value() == '90s':
            return queryset.filter(
                birthday__gte=date(1990, 1, 1),
                birthday__lte=date(1999, 12, 31),
            )

class PersonAdmin(admin.ModelAdmin):
    list_filter = (DecadeBornListFilter,)