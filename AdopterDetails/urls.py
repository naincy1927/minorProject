from django.urls import path
from AdopterDetails import views

urlpatterns = [
    path('', views.userPage , name = "userDetails"  ),]