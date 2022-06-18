from django.shortcuts import render, redirect
from datetime import datetime
import csv
import os


def home(request):
    return redirect('https://d1lrj6wbfx1cf6.cloudfront.net')


def formdata(request):
    if request.method == 'POST':
        f = open(f'{os.path.dirname(__file__)}/../../data/data.csv', 'a', newline='')
        wr = csv.writer(f)
        clientID = request.POST['clientID']
        center = request.POST['center']
        equipment = request.POST['gridRadios']
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        wr.writerow([clientID, center, equipment, time])
    return render(request, 'index.html')