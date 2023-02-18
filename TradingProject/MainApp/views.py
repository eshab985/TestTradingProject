from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import csv
import math
from processing import executor
# Create your views here.

def index(request):
    return render(request, 'index.html')

def download(request):
    print('Entered Download')
    json = {}
    if request.method == 'POST':  
        tf = request.POST.get('timeframe')
        print('Timeframe = ',tf)
        json = executor('nifty_data.csv', tf )
        print(json)
        return HttpResponse(json)
    else:
        return HttpResponse(json)
    
