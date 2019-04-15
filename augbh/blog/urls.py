from django.urls import path
from . import views
from blog import views

from .views import emailView, successView

#url for pages
urlpatterns = [
	path('events/', views.events, name="events"),
	path('contact/', views.contact, name="contact"),
	path('', views.index, name="index"),
	path('post1/', views.post1, name="post1"),
	path('post2/', views.post2, name="post2"),
	path('post3/', views.post3, name="Post3"),
	path('email/', emailView, name="email"),
	path('success/', successView, name="success"),
]