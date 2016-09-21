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
	
def go(request):
    global  i
    i= i+ 1
    return render_to_response(('gostruct.html',{}))

#python and django 
def python(request):
    global  i
    i= i+ 1
    return render_to_response(('python.html',{}))   

def django(request):
    global  i
    i= i+ 1
    return render_to_response(('django.html',{}))	
	
def version(request):
    global  i
    i= i+ 1
    return render_to_response(('version.html',{}))	
def gopackage(request):
    global  i
    i= i+ 1
    return render_to_response(('gopackage.html',{}))		
#yangming 's dream	
def fudan(request):
    global  i
    i= i+ 1
    return render_to_response(('fudan.html',{}))     

def fiveyearplan(request):
    global  i
    i= i+ 1
    return render_to_response(('fiveyearplan.html',{}))		
def everyday(request):
    global  i
    i= i+ 1
    return render_to_response(('everyday.html',{}))         

def dream2016(request):
    global  i
    i= i+ 1
    return render_to_response(('dream2016.html',{}))     	

def slice(request):
    global  i
    i= i+ 1
    return render_to_response(('slice.html',{}))		

def format(request):
    global  i
    i= i+ 1
    return render_to_response(('format.html',{}))	
def csintro(request):
    global  i
    i= i+ 1
    return render_to_response(('csintro.html',{}))     	
		
def htmllayoutexp(request):
    global  i
    i= i+ 1
    return render_to_response(('htmllayoutexp.html',{}))	
 #about server
def serverdev(request):
    global  i
    i= i+ 1
    return render_to_response(('server.html',{}))     


# About Linux
def linux(request):
    global  i
    i= i+ 1
    return render_to_response(('linux.html',{}))    

def linuxcommand(request):
    global  i
    i= i+ 1
    return render_to_response(('linuxfrequentcommands.html',{}))    

# About GOLANG
def pointerbasic(request):
    global  i
    i= i+ 1
    return render_to_response(('pointerbasic.html',{}))        

def gopaper(request):
    global  i
    i= i+ 1
    return render_to_response(('gopaper.html',{}))  



def image(request):
    global  i
    i= i+ 1
    return render_to_response(('image.html',{}))    
def someone(request):
    global  i
    i= i+ 1
    return render_to_response(('someone.html',{}))  

def struct2json(request):
    global  i
    i= i+ 1
    return render_to_response(('struct2json.html',{}))		

#yangming's front
def front(request):
    global  i
    i= i+ 1
    return render_to_response(('front.html',{}))          

def canvas(request):
    global  i
    i= i+ 1
    return render_to_response(('canvas.html',{})) 


def imagelayout(request):
    global  i
    i= i+ 1
    return render_to_response(('imagelayout.html',{}))   

def sublime(request):
    global  i
    i= i+ 1
    return render_to_response(('sublime.html',{}))  


#go network programming
def gonetwork(request):
    global  i
    i= i+ 1
    return render_to_response(('gonetwork.html',{}))  


#web map
def webmap(request):
    global  i
    i= i+ 1
    return render_to_response(('webmap.html',{}))  


#db
def db(request):
    global  i
    i= i+ 1
    return render_to_response(('db.html',{}))  

def sql(request):
    global  i
    i= i+ 1
    return render_to_response(('sql.html',{}))      
#ds
def ds(request):
    global  i
    i= i+ 1
    return render_to_response(('ds.html',{})) 
	
def test(request):
    global i
    i = i + 1
    dat = Reading.objects.last()
    ti = datetime.now()
    visitor_ip = request.META['HTTP_X_FORWARDED_FOR']  # try get visitor ip
    # context = {}
    # context['data']=dat
    # return HttpResponse(request,'index.html',context)
    ip = get_ip(request)
    url = 'http://ip-api.com/json/' + str(ip)
    r = requests.get(url).json()
    ip_pool.append(ip)

    visitor_people = 'You Are The' + str(i) + 'st  ' + 'Visitor'
    if ip is not None:
        print("we have an IP address for user")
    else:
        print("we don't have an IP address for user")
    return render_to_response('index.html', {'data': ti,'weather':dat ,'visitor_ip':ip,'count_visitor':visitor_people,'more_info':r})