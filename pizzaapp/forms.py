from django import forms
from .models import OrderPizza,CountPizza

class OrderPizzaForm(forms.ModelForm):
    class Meta:
        model = OrderPizza
        labels = {"topping_1": "Topping 1", "topping_2":"Topping 2"}
        fields = "__all__"

class CountPizzaForm(forms.ModelForm):
    class Meta:
        model = CountPizza
        fields = "__all__"