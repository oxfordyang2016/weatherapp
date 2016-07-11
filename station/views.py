from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpRequest
from django.http import HttpResponse
from datetime import datetime
#from django.tmplate.response import TempalteResponse
from station.models import Reading

def home(request):
    dat = Reading.objects.last()
    ti = datetime.now()
    visitor_ip = request.META['HTTP_X_FORWARDED_FOR']#try get visitor ip
    #context = {}
    #context['data']=dat
    #return HttpResponse(request,'index.html',context)
    return render_to_response('index.html', {'data': ti,'weather':dat ,'visitor':visitor_ip})