"""weatherapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import station.views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',station.views.home ,name='home'),
    url(r'^server/$',station.views.server,name='server'),
    url(r'^test/$',station.views.test,name='test'),
	url(r'^version/$',station.views.version,name='version'),	
	url(r'^format/$',station.views.format,name='format'),
    url(r'^sublime/$',station.views.sublime,name='sublime'),
	url(r'^struct2json/$',station.views.struct2json,name='struct2json'),
    #yangming's webmap
    url(r'^webmap/$',station.views.webmap,name='webmap'),
    #yangming's computer intro
     url(r'^csintro/$',station.views.csintro,name='csintro'),
    #yangming's python anddjango
     url(r'^python/$',station.views.python,name='python'),
    url(r'^django/$',station.views.django,name='django'),
    #yangming's git
    url(r'^gitrelease/$',station.views.gitrelease,name='gitrelease'),
    url(r'^gitsheet/$',station.views.gitsheet,name='gitsheet'),
     #front web design
    url(r'^front/$',station.views.front,name='front'),
    url(r'^imagelayout/$',station.views.imagelayout,name='imagelayout'),
    url(r'^pointerbasic/$',station.views.pointerbasic,name='pointerbasic'),
    #yangming's now
    url(r'^dream2016/$',station.views.dream2016,name='dream2016'),
    url(r'^someone/$',station.views.someone,name='someone'),
    url(r'^dream/$',station.views.fiveyearplan,name='fiveyearplan'),
    url(r'^fudan/$',station.views.fudan,name='fudan'),
    url(r'^everyday/$',station.views.everyday,name='everyday'),
    url(r'^startswiss/$',station.views.startswiss,name='startsiwss'),
    url(r'^psychology/$',station.views.psychology,name='psychology'),
    url(r'^tech/$',station.views.tech,name='tech'),
    #yangming's linux
     url(r'^linux/$',station.views.linux,name='linux'),
      url(r'^linuxcommand/$',station.views.linuxcommand,name='linuxcommand'),
     #yangming's go 
     url(r'^go/$',station.views.go ,name='go'),
    url(r'^gopackage/$',station.views.gopackage,name='gopackage'),
    url(r'^slice/$',station.views.slice,name='slice'),
    url(r'^gopaper/$',station.views.gopaper,name='gopaper'),
    #yangming's db 
     url(r'^db/$',station.views.db ,name='db'),
     url(r'^sql/$',station.views.db ,name='sql'),
     #yangming's ds
     url(r'^ds/$',station.views.ds ,name='ds'), 
     #yangming's english
     url(r'^english/$',station.views.english ,name='english'), 

     #yangming's Network program with go
     url(r'^gonetwork/$',station.views.gonetwork,name='gonetwork'),
     #yangming's canvas
     url(r'^canvas/$',station.views.canvas,name='canvas'),
      url(r'^serverdev/$',station.views.serverdev,name='serverdev'),
	]
