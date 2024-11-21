from django.contrib import admin
from . models import Customer, Product, Cart, OrderPlaced, Payment

# Register your models here.

@admin.register(Product)
class CakeModelAdmin(admin.ModelAdmin):
    list_display= ['id','title','discounted_price','category','product_image']
    
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display= ['id','user','locality','city','state','zipcode']
    
@admin.register(Cart)   
class CartModelAdmin(admin.ModelAdmin):
   list_display = ['id','user','product','quantity']
   
@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','amount','razorpay_order_id','razorpay_payment_status','razorpay_payment_id']
    
@admin.register(OrderPlaced)
class OrderePlacesModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status','payment']
 