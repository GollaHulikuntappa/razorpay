from django.shortcuts import render
from src.forms import CoffeePaymentForm
from src.models import ColdCoffee
from razorpay import Client

# Create your views here.

def coffee_payment(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100
        
        # Create Razorpay client
        client = Client(auth=('rzp_test_u9hpVee0gFqqYP', 'SIncjatkTSjecl0qEgPAOkj0'))
        
        # Create order
        response_payment = client.order.create(dict(amount=amount, currency="INR"))
        
        # print(response_payment)
        
        order_id= response_payment['id']
        order_status=response_payment['status']
        
        if order_status == 'created':
            cold_coffee=ColdCoffee(
                name=name,
                amount=amount,
                order_id=order_id
            )
            cold_coffee.save()
            
            response_payment['name']=name
            
            form = CoffeePaymentForm(request.POST or None)
            return render(request, "coffee_payment.html", {'form': form,'payment':response_payment})
    
    form = CoffeePaymentForm()
    
    return render(request, "coffee_payment.html", {'form': form})


def payment_status(request):
    response = request.POST
    
    print(response)
    return render(request,"payment_status.html")
