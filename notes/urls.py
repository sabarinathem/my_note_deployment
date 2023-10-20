from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('notes/<int:sid>/',views.notes,name="notes"),
]
