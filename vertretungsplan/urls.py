from django.conf.urls import url                                                        #Imortierung der Lib. url (=Pfadeingabe)   

from views import app_time_api,html_api,user_mask,app_table_api,logout,html_api_table   #Importierung der "view" Funktionen, siehe Code             
urlpatterns = [                                                                         #Erstellung des urlpatterns, mit einbindung an das Django Framework
               url(r'^$',app_time_api,name="start"),                                    #url "start", ruft die Funktion "app_time-api" auf                  
               url(r"open/$",html_api,name="html"),                                     #url "open", ruft die Funktion "html_api" auf    
               url(r"log/$",user_mask.as_view(),name="log"),                            #url "log", ruft die Funktion "user_mask.as_view" auf                     
               url(r"table/$",app_table_api,name="table"),                              #url "table", ruft die Funktion "app_table_api" auf            
               url(r"h/$",html_api_table,name="html_api_table"),                        #url "h", ruft die Funktion "html_api_table" auf                             
               
               url(r"logout/$",logout,name="logout"),                                   #url "logout", ruft die Funktion "logout" auf              
               
               
               ]
