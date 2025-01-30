from django.shortcuts import render

# Create your views here.

def coffee_payment(request):
    return render(request,"coffee_payment.html")
