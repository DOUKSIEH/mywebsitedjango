#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Bonjour tous le monde, La page d'accueil de l'appli des sondages.")

