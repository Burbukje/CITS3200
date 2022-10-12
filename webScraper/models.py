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
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, default=-31.9524993)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, default=115.8612164)
    parcel_address = models.CharField(max_length=128, null=True, default="")
    formatted_address = models.CharField(max_length=128, null=True, default="")
    phone = models.CharField(max_length=15, null=True, default="")
    website = models.CharField(max_length=128, null=True, default="")
    menu = models.BooleanField(default=False, null=True)
    opening_hours = models.JSONField(default=dict, null=True)

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
        return f'{year}-{self.business_id.get_name()} (Class: {self.get_class()} Category: {self.get_cat_one()})'

    def get_class(self) -> str:
        return self.classification
        
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