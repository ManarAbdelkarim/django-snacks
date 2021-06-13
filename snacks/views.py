from django.shortcuts import render
from django.views.generic import TemplateView
from .models import data_base 
from django.http import HttpResponse

# class HomePageView(TemplateView):
#     template_name='home.html'
#     all_data = data_base.objects.all()
#     print(all_data)
#     render(request, 'home.html', { 'all_data': {all_data}})

class AboutView(TemplateView):
    template_name = 'about.html'

def home(request):
    
        all_data = data_base.objects.all()[0]
        print(all_data)
        return render(request, 'home.html', { 'all_data': {all_data}})