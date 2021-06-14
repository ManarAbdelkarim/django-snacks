from django.urls import path
from .views import  AboutView , home  #,HomePageView

urlpatterns=[
    # path('', HomePageView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('', home, name='home')
]
