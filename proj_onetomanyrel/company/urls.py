from django.urls import path
from company import views

urlpatterns = [
    path('', views.home),
]
