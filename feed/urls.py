from django.urls import path
from . import views

urlpatterns = [
    path('', views.getEntries, name='getEntries'),
    path('newEntry', views.newEntry, name='newEntry')
]
