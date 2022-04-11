from typing import List
from django.shortcuts import render
from django.views.generic import ListView
from .models import Grain

# class MainList(ListView):
#     model = Grain
#     templat_name = 'main/home.html'

def Homepage(request) :
    return render(request,'main/home.html')

def chart_bar(request):
    return render(request,"main/chart.html")

class GrainList(ListView):
    model = Grain

