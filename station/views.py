from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpRequest
from django.http import HttpResponse
from datetime import datetime
import requests
#from django.tmplate.response import TempalteResponse
from station.models import Reading
from ipware.ip import get_ip
ip_pool = []
#as visitor count
i=0
def home(request):
    global i
    i = i+1
    dat = Reading.objects.last()
    ti = datetime.now()
    visitor_ip = request.META['HTTP_X_FORWARDED_FOR']#try get visitor ip
    #context = {}
    #context['data']=dat
    #return HttpResponse(request,'index.html',context)
    ip = get_ip(request)
    url = 'http://ip-api.com/json/'+str(ip)
    r = requests.get(url).json()
    ip_pool.append(ip)

    visitor_people = 'You Are The'+str(i) +'st  '+'Visitor'
    if ip is not None:
        print("we have an IP address for user")
    else:
        print("we don't have an IP address for user")
    return render_to_response('index.html', {'data': ti,'weather':dat ,'visitor_ip':ip,'count_visitor':visitor_people,'more_info':r})

def server(request):
    global  i
    i= i+ 1
    return render_to_response(('storyofshanghai.html',{}))
def git(request):
    global  i
    i= i+ 1
    return render_to_response(('git.html',{}))