from django.shortcuts import render
from django.http import HttpResponse
import base64
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.template import engines,RequestContext,loader
from django.template.context_processors import csrf



from stundenplan.models import *
from models import Plan
from django.http.response import JsonResponse, HttpResponseRedirect
# Create your views here.
import re
import json 
from aetypes import template
from django.views.generic.base import TemplateView
from django.contrib.auth.views import redirect_to_login

comp = re.compile(r"(\d+)?")
# compile (S or L and the the number, decide which of the is a student or teacher )

def authenticate(username,password):
    bool = None 
    try:
        Person_id = (comp.search(username).group())
    
        people = Person.objects.get_by_natural_key(Person_id)
        if (people.password == password):
            bool = people.pk
    except:
        bool = None
    finally:
        return bool
    """
    if student :
        return Stunden.object.get(id)
    if lehrer : 
        retunr Lehrer.object.get(id)
    
    """
#def rest_authenticate(username,password):
    
    
    
    
    
    
    
    
    
def bcx(f):
    def g(request,*args,**kwargs):

        if request.META.get("HTTP_AUTHORIZATION",False):
            authtype , auth = request.META["HTTP_AUTHORIZATION"].split()
            auth = base64.b64decode(auth)
            username,password = auth.split(":")
            print username+"#"+password
            auths = authenticate(username=username,password=password)
            if(auths):
                
                kwargs["user"] = auths
                

            

                return f(request,*args,**kwargs)
            else :
                    
                r = HttpResponse(str("nope"),status = 401)

                r["WWW-Authenticate"] = "Basic realm='bats'"
                return r
            
        r = HttpResponse(str("fotze bis nicht angemeldet"),status = 401)
        r["WWW-Authenticate"] = "Basic realm='batx'"
        return r
    return g


    
def session_reader(f):
    def g(request,*args,**kwargs):
        if (request.session.get("log") == "in"):
            return f(request,*args,**kwargs)
        return HttpResponseRedirect("../log")
        
            
        
    return g


def logout(request,*args,**kwargs):
    try:
        del(request.session["log"])
    except : 
        pass
        #maybe login 
        #
        #
    finally: 
        return HttpResponseRedirect("../log")





@bcx
def app_time_api(request,*args,**kwargs):
    
    
    #data = serialize("json",Raum.objects.all())
    d = dict()
    pers = Person.objects.get_by_natural_key(kwargs["user"])
    response = json.JSONDecoder().decode(serialize("json", Plan.objects.get_now(),use_natural_foreign_keys=True,use_natural_primary_keys=True))
    user = json.JSONDecoder().decode(serialize("json", [pers],use_natural_foreign_keys=True,use_natural_primary_keys=True))
    d.update({"content":response,"user":user})
    return JsonResponse(d)#render(request,"/Users/bcy-3/Developer/tls/static/layout.html",{})

@session_reader
def html_api(request,*args,**kwargs):
    
    query_rest = serialize("json", Plan.objects.get_now(),use_natural_foreign_keys=True,use_natural_primary_keys=True)
    s = json.JSONDecoder().decode(query_rest)
    # order queries
    #
    #
    
  
    
    return HttpResponse(render(request,"layout.html",{"d":s}))


@bcx 
def app_table_api(request,*args,**kwargs):
    
    d = dict()
    pers = Person.objects.get_by_natural_key(kwargs["user"])
    #
    #make filtering to 
    
    
    response = json.JSONDecoder().decode(serialize("json", Unterrichtsplan.objects.filter(personas=pers),use_natural_foreign_keys=True,use_natural_primary_keys=True))
    user = json.JSONDecoder().decode(serialize("json", [pers],use_natural_foreign_keys=True,use_natural_primary_keys=True))
    d.update({"content":response,"user":user})
    
    return JsonResponse(d)
    
    
   
    
    
    
@session_reader
def html_api_table(request,*args,**kwargs):
    #
    #
    # add html view of stundenplan and make unique view of the user per Stundeplan.objects.get("user_id")
    d = dict()
    pers = Person.objects.get_by_natural_key(int(request.session["user"]))
    
    
    response = json.JSONDecoder().decode(serialize("json", Unterrichtsplan.objects.filter(personas=pers),use_natural_foreign_keys=True,use_natural_primary_keys=True))
    
    

    #user = json.JSONDecoder().decode(serialize("json", [pers],use_natural_foreign_keys=True,use_natural_primary_keys=True))
    #d.update({"content":response,"user":user})
    
    
    
    h = HttpResponse(render(request,"layout_stundenplan.html",{"d":response}))
    return h
    
    
        
    

class user_mask(TemplateView):
    def  get(self,request,*args,**kwargs):
        
        if ("log" in request.session):
            if (request.session["log"] == "in"):
                return HttpResponseRedirect("../open")
        

        
        
        c = dict()
        c.update(csrf(request))
        h = HttpResponse(render(request,"log.html",{}))
        h["csrf"] = c
        return HttpResponse(h)
    
    def post(self,request,*args,**kwargs):
        user_pk = authenticate(request.POST["username"], request.POST["password"])
        
        if user_pk:
            h = HttpResponseRedirect("../open")
            request.session["log"] = "in"
            request.session["user"] = user_pk
            
            return h # to timetable 
        

        a = HttpResponseRedirect("../log")
        return a