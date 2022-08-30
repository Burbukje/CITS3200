from django.db import models
import uuid
from webScraper.classification_enums import *

# Create your models here.

class Collection_Year(models.Model):
    year = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.year)


class Local_Government(models.Model):
    year = models.ForeignKey(Collection_Year, on_delete=models.CASCADE)
    local_government_area = models.CharField(max_length=128, primary_key=True)

    def __str__(self):
        return self.local_government_area


class Business(models.Model):
    local_government_area = models.ForeignKey(Local_Government, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business_name = models.CharField(max_length=128)
    notes = models.TextField(max_length=256)

    def __str__(self):
        return self.business_name


class Contact_Details(models.Model):
    business_id = models.ForeignKey(Business, on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=18, decimal_places=15)
    latitude = models.DecimalField(max_digits=18, decimal_places=15)
    parcel_address = models.CharField(max_length=128)
    formatted_address = models.CharField(max_length=128)
    phone = models.CharField(max_length=15)
    website = models.CharField(max_length=128)
    menu = models.BooleanField(default=False)
    opening_hours = models.JSONField()

    def __str__(self):
        return str(self.business_id)


class Classification(models.Model):
    business_id = models.ForeignKey(Business, on_delete=models.CASCADE)
    classification = models.CharField(max_length=1, choices=Classification_Appendix.choices, default="")
    
    category_one = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    sub_cat_one = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    category_two = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    sub_cat_two = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    category_three = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    sub_cat_three = models.DecimalField(max_digits=4, decimal_places=2, null=True)

    def __str__(self):
        if self.category_one is None:
            return f'{self.classification}'
        else:
            return f'{self.classification}{self.category_one}'