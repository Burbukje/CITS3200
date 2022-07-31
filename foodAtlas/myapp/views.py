from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Model Veiw Controller (MVC)
# Create your views here.

# Hard coded for testing
def hello(request):
    text = """<h1>Welcome to the Food Atlas Project</h1>"""
    return HttpResponse(text)


# Model Veiw Template (MVT)
def hello_render(request):
    today = datetime.now()
    return render(request, "hello.html", {"today" : today})


# Accepting Parameters
def hello_param(request, param):
    text = "<h1>welcome to my app number %s!</h1>"% param
    return HttpResponse(text)