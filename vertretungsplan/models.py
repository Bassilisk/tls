from django.db import models


from stundenplan.models import *
from datetime import datetime

class PlanB(models.Manager):
    def get_now(self):
        return self.filter(day=datetime.now())

                
class Plan(models.Model):
    objects = PlanB()
    
    day = models.DateField()
    Unterricht = models.ForeignKey(Unterrichtsplan)
    std = models.IntegerField(choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)))
    erzsetzt_durch = models.ForeignKey(Lehrer)
    bemerkung =  models.CharField(max_length=120)
    def __unicode__(self):
     
        return str(self.day)+"_("+str(self.std)+")_"+str(self.Unterricht.Unterrict.unterrichtsfach)
    class Meta:
        ordering = ['std']
 
    
    
    
