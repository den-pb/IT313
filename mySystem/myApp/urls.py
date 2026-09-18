from django.urls import re_path
from myApp import views

urlpatterns = [
    re_path(r'^welcome/$', views.welcomepage),
    re_path(r'^welcomeform/$', views.welcomeformpage),
    re_path(r'^register/$', views.register),
    re_path(r'^mdas/$', views.mdas),
]