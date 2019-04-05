"""
from django.conf.urls import url
from . import views

from blog import views

#url for pages
urlpatterns = [
	path(r'^events$', views.events, name='events.html'),
	url(r'^$', views.index, name='index.html'),
	url(r'^post1$', views.post1, name='post1.html'),
	url(r'^post2$', views.post2, name='post2.html'),
	url(r'^post3$', views.post3, name='Post3.html'),
]
"""

#compare how you have written your code with how it could be done better
from django.urls import path

#from the current directory import view
from . import views

urlpatterns = [
	path('events/', views.events, name='events'),
	path('post1/',  views.post1,  name='post1'),
    path('post2/',  views.post2,  name='post2'),
	path('post3/',  views.post1,  name='post3'),
]
