from django.urls import path
from . import views

urlpatterns = [
    path('JJK/', views.JJK, name='JJK'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('BTS/<str:name>/', views.BTS, name='BTS'),
]