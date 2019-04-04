from django.urls import path
from . import views
from blog import views

#url for pages
urlpatterns = [
	path('events/', views.events, name="events"),
	path('', views.index, name="index"),
	path('post1/', views.post1, name="post1"),
	path('post2/', views.post2, name="post2"),
	path('post3/', views.post3, name="Post3"),
]