from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='index'),
	path('projects/', views.projects, name='projects'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
	path('projects/safar_details/', views.safar_details, name='safar_details'),
	path('projects/irishcribs_details/', views.irishcribs_details, name='irishcribs_details'),
	path('projects/thiswebsite_details/', views.thiswebsite_details, name='thiswebsite_details'),
]
