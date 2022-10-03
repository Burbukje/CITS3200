from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
import openpyxl

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