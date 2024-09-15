from django.shortcuts import render , HttpResponse , get_object_or_404 , redirect
from .models import *
from django.utils.datastructures import MultiValueDictKeyError

def home(request):
    if 'key' in request.POST and request.POST['key']:
        pass
    else:
        try:
            url_view = request.POST.get('url')
            name_view = request.POST.get('name')
            time_of_event_view = request.POST.get("time")
            venue_of_event_view = request.POST.get("venue")
            details_of_event_view = request.POST.get("details")
            info = Event(name_of_event=name_view ,qr_code=url_view, time_of_event=time_of_event_view , venue_of_event=venue_of_event_view , details_of_event=details_of_event_view)
            info.save()
        except:
            url_view = request.POST.get('url')
            name_view = request.POST.get('name')
            time_of_event_view = request.POST.get("time")
            venue_of_event_view = request.POST.get("venue")
            details_of_event_view = request.POST.get("details")
            info = Event(name_of_event=name_view ,qr_code=url_view, time_of_event=time_of_event_view , venue_of_event=venue_of_event_view , details_of_event=details_of_event_view)
            info.save()
            
    Events = Event.objects.all()
    return render(request , "index.html", {"events":Events})

def qrcode(request , modal_name ,pk):
    if modal_name == 'event':
        model = get_object_or_404(Event, pk=pk)
        
    Events = Event.objects.all()
    context = {'model': Events}
    return render(request , 'display.html', context)