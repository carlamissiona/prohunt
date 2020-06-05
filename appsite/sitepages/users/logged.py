from django.http import HttpResponse
# from django.views import View
from django.views.generic.base import TemplateView , View

from django.views.generic import ListView, DetailView
from appsite.models import Field, Category
from appsite import google


class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'object_list'
    model = Field
    def get_queryset(self):
    	google.googlemain()
    	#Feature before accessing home call google authentication 
    	#Feature but google logged in must be the email of the registered user 

    	query_objects = { 'fields' : Field.objects.all() , 'category' : Category.objects.all() , }
    	return query_objects

 