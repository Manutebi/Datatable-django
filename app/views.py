from django.shortcuts import render

from airtable import Airtable

def home(request):

    return render(request, 'app/home.html')

def home(request):
    airtable = Airtable('appU7lYsFSoNH4hGO', 'Productos', 'keykY5YjFxN23izT6')
    data = airtable.get_all()
    return render(request, 'app/home.html', {'data': data})


    