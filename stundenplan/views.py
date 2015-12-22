from django.shortcuts import render          #Import der Funktion "render", wird benötigt um ein html layout mit variablen zu referenzieren
from django.http import HttpResponse         #Import der Klasse "HttpResponse",wird benötigt um eine Http anfrage zu beantworten      
# Create your views here.

def get_time_table(request):                #Funktion "get_time_table" wird mit der Variable "request" (http Header und Body) aufgerufen               
    render(request,"static/layout.html",{}) #gibt die Datei Layout html mit zugewiesenen Variablen zurück    
    
