from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('dtl/', views.dtl, name='dtl'),
    path('greeting/', views.greeting),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch),
    path('hello/<str:name>/', views.hello),
]