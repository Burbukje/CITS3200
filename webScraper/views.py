from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
import openpyxl
from webScraper.scraper import *
import xlwt
from django.http import HttpResponse
from webScraper.downloader import *
from webScraper.uploader import *
from django.template import loader

SUCCESS = 0
FAIL = 1

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("uploader")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("index")


def uploader(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == "POST" and "excel_file" in request.FILES.keys():
            lga = request.POST.get("lga")
            year = request.POST.get("year")
            excel_file = request.FILES["excel_file"]
            uploaded = add_excel_to_db(excel_file, lga, year)
            #uploaded = 0
            template = loader.get_template("uploader.html")
            context = {
                'uploaded': uploaded,
            }
            return HttpResponse(template.render(context, request))
        else:
            return render(request, "uploader.html", {})


def downloader_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    else:
        if request.method == "GET" and not request.GET.get("q") == None and not request.GET.get("q") == "":
            return download_excel_data(request)
        else:
            return render(request, "downloader.html")


def download_excel_data(request):
    # content-type of response
    response = HttpResponse(content_type='application/ms-excel')

    #decide file name
    response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'

    #creating workbook
    wb = xlwt.Workbook(encoding='utf-8')

    #adding sheet
    ws = wb.add_sheet("sheet1")

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    # headers are bold
    font_style.font.bold = True

    #column header names, you can use your own headers here
    columns = [
    "local_government_area",
    "collection_year",
    "business_name",
    "classification_name",
    "category_1",
    "sub_category_1",
    "category_2",
    "sub_category_2",
    "category_3",
    "sub_category_3",
    "y_latitude",
    "x_longitude",
    "original_lga_provided_address",
    "formatted_address",
    "contact_1",
    "contact_2",
    "email",
    "website",
    "menu_(yes,_provided_on_website/no)",
    "children's_menu_provided_(yes/no)",
    "opening_hours",
    "notes",
]

    #write column headers in sheet
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    #get your data, from database or from a text file...
    #data = get_data() #dummy method to fetch data.
    lga = "ARMADALE, CITY OF"
    year = 2022
    data = get_lga_to_excel(lga=lga, year=year)
    for my_row in data:
        row_num = row_num + 1
        # LGA
        ws.write(row_num, 0, lga, font_style)
        # Collection year
        ws.write(row_num, 1, year, font_style)
        # Business Name
        ws.write(row_num, 3, my_row.get_name(), font_style)

        curr_classes = Classification.objects.filter(business_id=my_row)[0]
        # Classification
        ws.write(row_num, 4, curr_classes.get_class(), font_style)
        # Categories
        ws.write(row_num, 5, curr_classes.get_cat_one(), font_style)

        curr_contact = Contact_Details.objects.filter(business_id=my_row)[0]
        # latitude
        ws.write(row_num, 10, curr_contact.get_lat(), font_style)
        # longitude
        ws.write(row_num, 11, curr_contact.get_long(), font_style)
        # Orginal add
        ws.write(row_num, 12, curr_contact.get_parcel_add(), font_style)
        # formatted add
        ws.write(row_num, 13, curr_contact.get_formatted_add(), font_style)
        # contact 1
        ws.write(row_num, 14, curr_contact.get_phone(), font_style)
        # website
        ws.write(row_num, 17, curr_contact.get_website(), font_style)
        # opening hours
        ws.write(row_num, 20, curr_contact.get_opening(), font_style)

    wb.save(response)
    return response