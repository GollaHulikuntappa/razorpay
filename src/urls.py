from django.urls import path
from src.views import coffee_payment

urlpatterns = [
    path('', coffee_payment, name='coffee-payment'),
]