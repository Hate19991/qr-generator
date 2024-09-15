from django.db import models

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_event = models.CharField(max_length= 35)
    time_of_event = models.CharField(max_length=5)
    venue_of_event = models.TextField()
    details_of_event = models.TextField()
    qr_code = models.TextField()
    