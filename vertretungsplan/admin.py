from django.contrib import admin

from models import Plan

# Register your models here.


class PlanAdmin(admin.ModelAdmin):
    day = 'pub_date'
    list_display = ("day","Unterricht","std","erzsetzt_durch","bemerkung")
    actions  = "g"
    def g(self):
        return "f"
    #date_hierarchy = "pub_date"

admin.site.register(Plan,PlanAdmin)
