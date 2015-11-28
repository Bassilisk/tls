from django.db import models
from django.db.models.manager import Manager
class person(Manager):
    
    
    def get_by_natural_key(self,code):
        return self.get(id=code)
# Create your models here.
class Person(models.Model):
    objects = person()
    name = models.CharField(max_length=100)
    vorname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    
    
    def __unicode__(self):
        return str(self.id)+self.vorname
    def natural_key(self):
        return str(self.id)+self.vorname
    

class Subject(models.Model):
    
    unterrichtsfach = models.CharField(max_length=50,unique=True)
    
    
    def natural_key(self):
        return (self.unterrichtsfach,)
    def __unicode__(self):
        return self.unterrichtsfach

class Lehrer(Person):
    objects = person()
    facher = models.ManyToManyField("Subject")
  
    
    def natural_key(self):
        return (str(self.id)+self.name,)
    
class Raum(models.Model):
    
    nummer = models.CharField(max_length=10,unique=True)
    def __unicode__(self):
        return self.nummer
    def natural_key(self):
        return (self.nummer,)
        
    
    
class Schueler(Person):
    objects = person()
    jahrgang = models.IntegerField()
    klasse = models.CharField(max_length=5)

    
    
    
    
    


class Unterrichtsplan(models.Model):
    jahrgang = models.IntegerField()
    kurs = models.CharField(max_length=15)

    raum = models.ForeignKey(Raum)
    Unterrict = models.ForeignKey(Subject)
    tag = models.IntegerField(choices=((1,"Mo"),(2,"Di"),(3,"Mi"),(4,"Do"),(5,"Fr")))
    std = models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)))
    lehrer = models.ForeignKey(Lehrer)
    personas= models.ManyToManyField("Schueler")
    
    
    class Meta:
        ordering = ["tag","std"]
    


    

    
   
    
    
    def natural_key(self):
        return (self.std,self.raum.natural_key()[0],self.jahrgang)+self.Unterrict.natural_key()+self.lehrer.natural_key()
    def __unicode__(self):
        return self.Unterrict.unterrichtsfach+"_"+str(self.jahrgang)+"_"+self.kurs
    
    
    
"""
class Stundenplan(models.Model):
    persons = models.ForeignKey(Person,related_name="plans")
    unterrichts = models.ForeignKey(Unterrich,related_name="plans")
    
    
    pass# connect beetween Person and Unterricht many to many 

"""

    