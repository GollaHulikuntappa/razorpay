from django.contrib import admin
from src.models import ColdCoffee

class ColdCoffeeAdmin(admin.ModelAdmin):
    list_display=['name','amount','order_id','razorpay_payment_id','paid']

# Register your models here.

admin.site.register(ColdCoffee,ColdCoffeeAdmin)
