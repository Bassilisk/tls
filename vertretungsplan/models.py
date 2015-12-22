from django.db import models                                                                              #Importierung der "models" Klasse  


from stundenplan.models import *                                                                          #Importierung aller Datenbank "models" aus der Lib. Stundenplan          
from datetime import datetime                                                                             #Improtierung des Lib. "datetime" (Datums-, und Zeitbibilothek)                      

class PlanB(models.Manager):                                                                              #Erstellung der Klassen "Manager" (PlanB), benötigung für Steuerung der Klasse "Plan"                           
    def get_now(self):                                                                                    #Definition der Methode "get_now"                                  
        return self.filter(day=datetime.now())                                                            #gibt eine Selektion nach der Variable "day" unter der Bedingung des jetztigen datums ("datetime.now"), parallel zu SQL *WHERE DAY=datetime.now*                                  

                
class Plan(models.Model):                                                                                 #Vererbung der Klasse "models.Model", Integration mit dem Django Framework              
    objects = PlanB()                                                                                     #Integration durch die Variable "Objects" mit dem Manager                                                
    
    day = models.DateField()                                                                              #Erstellun der Variable "day" (SQL. Datefield)                                                                  
    Unterricht = models.ForeignKey(Unterrichtsplan)                                                       #Erstellung der Variable "Unterricht" mit dem Fremdschlüssel "Unterrichtsplan" von "Stundenplan"                 
    std = models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)))    #Erstellung der Variable "std" mit der Auswahl zwischen 1 bis 10 (Hash Map/Set)                                 
    erzsetzt_durch = models.ForeignKey(Lehrer)                                                            #Erstellung der Variable "ersetzt_durch" mit dem Fremdschlüssel "Lehrer" von "Stundenplan"          
    bemerkung =  models.CharField(max_length=120)                                                         #Erzeugung der Variable "bemerkung" (SQL. charfield), mit max. 120 Zeichen begrenzt                                         
    def __unicode__(self):                                                                                #Rückgabe des Objektes als Objektname                  
     
        return str(self.day)+"_("+str(self.std)+")_"+str(self.Unterricht.Unterrict.unterrichtsfach)       #Objektname besteht aus Tag, Stunde und Unterrichtsfach                                             
    class Meta:                                                                                           #Erstellung der Klasse Meta                      
        ordering = ['std']                                                                                #Sortierung nach "std" aufsteigend                              
 
    
    
    
