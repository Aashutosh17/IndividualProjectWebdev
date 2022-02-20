from django.urls import path

from . import views


urlpatterns = [

path('login', views.loginfn),
path('validation', views.validation)

]