from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage),
    path('helloPage/', views.helloPage),
    path('AddTwoNosPage',views.AddTwoNosPage),
    path('addition',views.additionTwoNos)
]
