from django.contrib import admin                                #


# Register your models here.
from models import *                                            #                

class PersonS(admin.ModelAdmin):                                #                        
    list_display = ("id","vorname","name","jahrgang","klasse")  #                             
class PersonL(admin.ModelAdmin):                                #                            
    list_display = ("id","vorname","name","facher")             #                                
    #list_display_linls = ("facher",)                           #                                         
    
    
admin.site.register(Subject)                                    #                           
admin.site.register(Lehrer,PersonL)                             #                                    
admin.site.register(Raum)                                       #                                     
admin.site.register(Unterrichtsplan)                            #                                                            
admin.site.register(Schueler,PersonS)                           #                                            
#admin.site.register(Stundenplan)


