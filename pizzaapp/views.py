from itertools import count
from multiprocessing import context
from django.shortcuts import render
from .models import OrderPizza
from .forms import CountPizzaForm, OrderPizzaForm

def home(request):
    return render(request,"pizzaapp/home.html",context)

def orderpage(request):
    form = OrderPizzaForm()
    count = CountPizzaForm()
    context = {
        "form" : form,
        "count": count
    }
    return render(request,"pizzaapp/orderpizza.html",context)


