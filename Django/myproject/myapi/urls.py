from django.urls import path
from . import views

urlpatterns = [
    path('getListItem/', views.getListItem, name='index'),
]
