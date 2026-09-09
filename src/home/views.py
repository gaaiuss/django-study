from typing import TYPE_CHECKING

from django.shortcuts import render

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse

# Create your views here.


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")
