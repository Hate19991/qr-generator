from django.contrib import admin
from .models import *

class EventAdmin(admin.ModelAdmin):
    list_display = ["id","name_of_event","venue_of_event","time_of_event" , "details_of_event" , "qr_code"]
    search_fields  = ["id","name_of_event","venue_of_event","time_of_event" , "details_of_event", "qr_code"]
    readonly_fields = ["id"]
    list_filter = ['id']

admin.site.register(Event , EventAdmin)