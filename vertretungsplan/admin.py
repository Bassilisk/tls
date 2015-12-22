from django.contrib import admin                                                #Importieren der Modul Klasse admin, benötigt für Modell Admin

from models import Plan                                                         #Importieren des selbst erstellten Modells "Plan"

# Register your models here.                                                            


class PlanAdmin(admin.ModelAdmin):                                              #Erstellung des Administrations Schnittstelle "PlanAdmin" mit Vererbung von "ModelAdmin"
    day = 'pub_date'                                                            #Sortierung nach Variable "pub_date", sortierung nach Datum aufsteigend 
    list_display = ("day","Unterricht","std","erzsetzt_durch","bemerkung")      #Projektion der Datenbank Variablen siehe zuordnung
    actions  = "g"                                                              #test einer funktion (unwichtig)                                                              
    def g(self):                                                                #test der  Funktion "g"
    return "f"                                                                  
    #date_hierarchy = "pub_date"                                                                

admin.site.register(Plan,PlanAdmin)                                             #Registrieung der Schnittstelle "PlanAdmin" an das Framework                    
