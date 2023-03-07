from django.shortcuts import render

from airtable import Airtable

def home(request):

    return render(request, 'app/home.html')

def home(request):
    airtable = Airtable('appTsErgl1kPnkWgl','Accounts', 'keykY5YjFxN23izT6')
    data = airtable.get_all()
    return render(request, 'app/home.html', {'data': data})
    
def login(request):

    return render(request, 'app/login.html')

def registro(request):

            return render(request, 'app/registro.html') 