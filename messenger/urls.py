from django.urls import path
from . import views

urlpatterns = [
    path('', views.sendMessageTest, name='sendMessageTest'),
    path('receive/', views.receiveMessage, name='receiveMessage')
]
