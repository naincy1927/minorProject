from django.urls import path
from Help import views

urlpatterns = [
    path('', views.helpPage , name = "Help"  ),]