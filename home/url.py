from django.urls import path
from home.views import BlogList
from . import views


urlpatterns = [
    path('register', views.register),
    path('publisher/', views.home),
    path('publishers/', BlogList.as_view()),
]


