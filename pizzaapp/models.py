from tkinter.tix import MAX
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


size_choices = [
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large')
]


class OrderPizza(models.Model):
    topping_1 = models.CharField(max_length=70)
    topping_2 = models.CharField(max_length=70)
    size = models.CharField(max_length=10, choices=size_choices)

    
    def __str__(self):
        return self.topping_1

class CountPizza(models.Model):
        count = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )