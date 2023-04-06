from django.urls import path
from Adopt import views

urlpatterns = [
    path('', views.AdoptPage , name = "adopt"  ),]