from django.db import models
from django.db.models.manager import Manager
class person(Manager):                                                  # wurde schon bei Vertretungsplan.models erstellt
    
    
    def get_by_natural_key(self,code):                                  #Funktion "get_by-natural_key" wird mit variable "code" aufgerufen
        return self.get(id=code)                                        #gibt ein Objekt mit der ID = Code wieder zurück (ähnlichkeiten wie Vertretungsplan.models)
# Create your models here.                                              
class Person(models.Model):                                             #Siehhe "Vertretungsplan.model"                                    
    objects = person()                                                  #"                                            
    name = models.CharField(max_length=100)                             #"                                   
    vorname = models.CharField(max_length=100)                          #"                               
    password = models.CharField(max_length=100)                         #"                                   
    is_active = models.BooleanField(default=False)                      #Variable "is_active" wird standartmäßig auf "false" gesetzt, sergej wird später noch einmal erklären                              
    
    
    def __unicode__(self):                                              #                    
        return str(self.id)+self.vorname                                #                                                
    def natural_key(self):                                              #ID wird mit dem Vornamen des Benutzer zurückgegeben                                
        return str(self.id)+self.vorname                                #return ID als String mit Kombination mit Kombination der Variable Vorname                                               
    

class Subject(models.Model):                                            #                
    
    unterrichtsfach = models.CharField(max_length=50,unique=True)       #"Unterrichtsfach" soll einmalig, durch unique=true, sein                                                    
    
            
    def natural_key(self):                                              #                                   
        return (self.unterrichtsfach,)                                  #return des Array mit Variable "..."                      
    def __unicode__(self):                                              #                                
        return self.unterrichtsfach                                     #return der Variable "unterrichtsfach", als Objektname                                                    

class Lehrer(Person):                                                   #wie bei vorherigen                                                    
    objects = person()                                                  #                                                                     
    facher = models.ManyToManyField("Subject")                          #variable "facher" wird mit dem Model (Subject) durch "ManytoMany" miteinander verknüpft; n zu m Beziehung                                                                                 
  
    
    def natural_key(self):                                              #siehe vorherige                                                                
        return (str(self.id)+self.name,)                                #                                                            
            
class Raum(models.Model):                                               #Erstellung des Models Raum, sehe Ähnlichkieten zu vorherigen                                                                                   
    
    nummer = models.CharField(max_length=10,unique=True)                #soll einmalig sein unique wie vorherig, raum nummer                                                                 
    def __unicode__(self):                                              #                                                    
        return self.nummer                                              #                                                
    def natural_key(self):                                              #                                                            
        return (self.nummer,)                                           #                                            
        
    
    
class Schueler(Person):                                                 # siehe vorherige                                                                             
    objects = person()                                                  #                                                                
    jahrgang = models.IntegerField()                                    #                                                    
    klasse = models.CharField(max_length=5)                             #                                    

    

class Unterrichtsplan(models.Model):                                    #wie vorherige auch
    jahrgang = models.IntegerField()                                    #                 
    kurs = models.CharField(max_length=50)                              #                                

    raum = models.ForeignKey(Raum)                                      #                        
    Unterrict = models.ForeignKey(Subject)                              #                                    
    tag = models.IntegerField(choices=((1,"Mo"),(2,"Di"),(3,"Mi"),(4,"Do"),(5,"Fr")))                                               
    std = models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)))                                      
    lehrer = models.ForeignKey(Lehrer)                                                  
    personas= models.ManyToManyField("Schueler")                                                        
    
    
    class Meta:                                                                 
        ordering = ["tag","std"]                                        #sortiert nach Tga und Stunde aufsteigend                                
    


    def natural_key(self):                                             #gibt array mit variablen zurück                             
        return (self.std,self.raum.natural_key()[0],self.jahrgang)+self.Unterrict.natural_key()+self.lehrer.natural_key()   #rückgabe der variablen (schnittstelle für andere funktionen)
    def __unicode__(self):                                             #                         
        return self.Unterrict.unterrichtsfach+"_"+str(self.jahrgang)+"_"+self.kurs
    
    
    
"""
class Stundenplan(models.Model):
    persons = models.ForeignKey(Person,related_name="plans")
    unterrichts = models.ForeignKey(Unterrich,related_name="plans")
    
    
    pass# connect beetween Person and Unterricht many to many 

"""

    
