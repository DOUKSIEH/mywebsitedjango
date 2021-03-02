#from django.shortcuts import render
from django.http import HttpResponse
import datetime

datedujour = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')

# Create your views here.
def index(request):
    return HttpResponse("Bonjour tous le monde, La page d'accueil de l'appli des sondages ({})".format(datedujour))

