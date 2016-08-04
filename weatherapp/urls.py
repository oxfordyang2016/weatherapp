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
    #yangming's django
    url(r'^django/$',station.views.django,name='django'),
    #yangming's git
    url(r'^git/$',station.views.git,name='git'),
     #front web design
    url(r'^front/$',station.views.front,name='front'),
    url(r'^imagelayout/$',station.views.imagelayout,name='imagelayout'),
    url(r'^pointerbasic/$',station.views.pointerbasic,name='pointerbasic'),
    #yangming's now
    url(r'^dream2016/$',station.views.dream2016,name='dream2016'),
    url(r'^someone/$',station.views.someone,name='someone'),
    url(r'^dream/$',station.views.fiveyearplan,name='fiveyearplan'),
    #yangming's linux
     url(r'^linux/$',station.views.linux,name='linux'),
     #yangming's go 
     url(r'^go/$',station.views.go ,name='go'),
    url(r'^gopackage/$',station.views.gopackage,name='gopackage'),
    url(r'^slice/$',station.views.slice,name='slice'),

 

     #yangming's Network program with go
     url(r'^gonetwork/$',station.views.gonetwork,name='gonetwork'),
     #yangming's canvas
     url(r'^canvas/$',station.views.canvas,name='canvas'),
      url(r'^serverdev/$',station.views.serverdevr,name='serverdev'),
	]
