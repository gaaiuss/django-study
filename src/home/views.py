from django.http import HttpRequest, HttpResponse

# from django.shortcuts import render

# Create your views here.


def home_view(request: HttpRequest) -> HttpResponse:
    print(request)
    return HttpResponse("This is the home view.")
