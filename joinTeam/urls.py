from django.urls import path
from joinTeam import views

urlpatterns = [
    path('', views.joinPage,name = "join")]