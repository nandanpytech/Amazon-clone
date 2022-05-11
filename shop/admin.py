from django.contrib import admin
from .models import Customer,Product,Cart,Orderplaced
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=["User","name","mobile","pin","state"]

@admin.register(Product)
class Productdmin(admin.ModelAdmin):
    list_display=["prname","price","brand"]

@admin.register(Cart)
class Cartdmin(admin.ModelAdmin):
    list_display=["User","product","qty"]    

@admin.register(Orderplaced)
class Orderplaceddmin(admin.ModelAdmin):
    list_display=["User","product","quantity","status"]      