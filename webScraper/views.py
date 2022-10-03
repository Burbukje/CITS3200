from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
import openpyxl
from webScraper.scraper import *
import xlwt
from django.http import HttpResponse

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
            excel_file = request.FILES["excel_file"]
            
#-----------------The following is just a sanity check----------------------
            # you may put validations here to check extension or file size
            # wb = openpyxl.load_workbook(excel_file)

            # getting a particular sheet by name out of many sheets
            # worksheet = wb.active
            # print(worksheet)

            # excel_data = list()
            # iterating over the rows and
            # getting value from each cell in row
            # for row in worksheet.iter_rows():
            #     row_data = list()
            #     for cell in row:
            #         row_data.append(str(cell.value))
            #     excel_data.append(row_data)
#------------------------------------------------------------------------

            return render(request, "uploader.html")

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
    columns = ['Column 1', 'Column 2', 'Column 3', 'Column 4', ]

    #write column headers in sheet
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    #get your data, from database or from a text file...
    #data = get_data() #dummy method to fetch data.
    data = [1, 2, 3]
    for my_row in data:
        row_num = row_num + 1
        # ws.write(row_num, 0, my_row.name, font_style)
        # ws.write(row_num, 1, my_row.start_date_time, font_style)
        # ws.write(row_num, 2, my_row.end_date_time, font_style)
        # ws.write(row_num, 3, my_row.notes, font_style)

    wb.save(response)
    return response