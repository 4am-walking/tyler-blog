from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request) -> HttpResponse:
    return render(request, "index.html")


def test(request) -> HttpResponse:
    return render(request, "inner-page.html")


def details(request) -> HttpResponse:
    return render(request, "portfolio-details.html")
