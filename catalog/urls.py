from django.urls import path
from catalog import views

urlpatterns = [
    
]

urlpatterns + [
    path('', views.index, name='index')
]