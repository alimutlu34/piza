from django.urls import path
from .views import home, orderpage

urlpatterns = [
    path("", home, name="home"),   
    path("orderpizza/",orderpage, name="orderpage"),   
]