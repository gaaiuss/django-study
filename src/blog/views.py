# from django.shortcuts import render

# Create your views here.

from django.http import HttpRequest, HttpResponse


def blog_view(request: HttpRequest) -> HttpResponse:
    print(request)
    return HttpResponse("This is the blog view.")
