from django.contrib import admin
from .models import Collection_Year, Contact_Details, Business, Local_Government, Classification

# Register your models here.

admin.site.register(Collection_Year)
admin.site.register(Contact_Details)
admin.site.register(Business)
admin.site.register(Local_Government)
admin.site.register(Classification)