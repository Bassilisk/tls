from django.conf.urls import url

from views import app_time_api,html_api,user_mask,app_table_api,logout,html_api_table
urlpatterns = [ url(r'^$',app_time_api,name="start"),
               url(r"open/$",html_api,name="html"),
               url(r"log/$",user_mask.as_view(),name="log"),
               url(r"table/$",app_table_api,name="table"),
               url(r"h/$",html_api_table,name="html_api_table"),
               
               url(r"logout/$",logout,name="logout"),
               
               
               ]