from django.urls import path
from . import views

urlpatterns = [
    path('passObject/', views.passObject),
]
