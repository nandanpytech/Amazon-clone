from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    mobile=models.IntegerField()
    pin=models.IntegerField()
    village=models.CharField(max_length=200)
    town=models.CharField(max_length=200)
    state=models.CharField(default="Karnatak",max_length=10)
    default=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    prname=models.CharField(max_length=200,default="")
    price=models.CharField(max_length=10000000000000,default="")
    brand=models.CharField(max_length=200,default="")
    image=models.ImageField(upload_to="photos")
    desc=models.CharField(max_length=250,default="")
    specify=models.CharField(max_length=250,default="")
    info=models.CharField(max_length=250,default="")
    size=models.CharField(max_length=120,default="")
    model=models.CharField(max_length=120,default="")
    storage=models.CharField(max_length=120,default="")

    def __str__(self):
        return self.prname

class Cart(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=1)  

    def __str__(self):
        return self.id

status=(
    ("Accepted","Accepted"),
    ("Packed","Packed"),
    ("Shipped","Shipped"),
    ("Delivered","Delivered"),
    ("Cancel","Cancel")
)
class Orderplaced(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    orderd_date=models.DateField(auto_now_add=True)
    status=models.CharField(choices=status,max_length=10 ,default="Pending")

    

