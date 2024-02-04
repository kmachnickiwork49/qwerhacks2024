from django.http import Http404
from django.shortcuts import render

from .models import *

def main(request):
    context = {}
    return render(request, "home/main.html", context)