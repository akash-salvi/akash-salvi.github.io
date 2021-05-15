from django.urls import path
from . import views

urlpatterns = [
       # Home page Url
       path('',views.home,name='home'),
      
]