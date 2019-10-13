from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('predict/', views.predict),
    path('form/',views.form),
    path('result/', views.result) , # -*- coding: utf-8 -*-

]