from django.http.response import HttpResponse
from .forms import CustomerRegistration,CustomerLogin,CustomerAddress
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models import Product,User,Customer,Cart,Orderplaced
# Create your views here.
def home(request):
    default_address=Customer.objects.filter(default=True)
    print(not(default_address))
    return render  (request,"html/Home.html",{"default_address":default_address})

def search_hole(request):
    query=request.GET['search']
    if len(query)>20:
        allProduct=Product.objects.none
    else:    
        listname=Product.objects.filter(prname__icontains=query)
        allProduct=listname
    default_address=Customer.objects.filter(default=True)
    params={'allProduct':allProduct,'query':query,'default_address':default_address}
    return render(request,"html/search-hole.html",params)

def selected_product(request,id):
    default_address=Customer.objects.filter(default=True)
    product=Product.objects.filter(id=id)
    params={'default_address':default_address,"product":product}
    return render(request,"html/selected_product.html",params)

def showformat(request):
        if request.method =="POST":
            fm=CustomerRegistration(request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['name']
                mob=fm.cleaned_data['mob']
                email=fm.cleaned_data['email']
                password=fm.cleaned_data['password']
                repassword=fm.cleaned_data['repassword']
                myuser=User.objects.create_user(uname,email,password)
                myuser.save()
            return redirect('/')   

        else:   
            fm=CustomerRegistration()
            return render(request,"html/sign-up.html",{'form':fm})

def loginformat(request): 
    if request.method == 'POST':
        fm=CustomerLogin(request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['name']
            password=fm.cleaned_data['password']
            user=authenticate(username=uname, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse("404 not found")    
    else:
        fm=CustomerLogin() 
        return render(request,"html/sign-in.html",{"form":fm})      

def logoutformat(request):
    logout(request)
    return redirect('/') 

@login_required(login_url='/sign-in/')
def buy(request,id):
    address=Customer.objects.filter(default=True)
    Customer_name=Customer.objects.get(default=True)
    product=Product.objects.filter(id=id)
    product_name=Product.objects.get(id=id)
    buy_item=Orderplaced.objects.create(User=request.user,product=product_name,Customer=Customer_name,quantity=1)
    buy_item.save()
    params={'address':address,"product":product}
    return render(request,"html/buy.html",params)       

@login_required(login_url='/sign-in/')
def cart(request,id):
    product=Product.objects.get(id=id)
    cart_item=Cart.objects.create(User=request.user,product=product,qty=1)
    cart_item.save()
    carts=Cart.objects.all()
    default_address=Customer.objects.filter(default=True)
    params={'carts':carts,'default_address':default_address}
    return render(request,"html/cart.html",params)    

def address(request):
    alladdress=Customer.objects.all()
    default_address=Customer.objects.filter(default=True)
    print(len(default_address)==0)
    para={'alladdress':alladdress,"default_address":default_address}
    return render(request,"html/address.html",para)     

def address_form(request):
    if request.method == 'POST':
        fm=CustomerAddress(request.POST)
        if fm.is_valid():
            name=fm.cleaned_data['name']
            mob=fm.cleaned_data['mob']
            pin=fm.cleaned_data['pin']
            village=fm.cleaned_data['village']
            town=fm.cleaned_data['town']
            state=fm.cleaned_data['state']
            address=Customer(User=request.user,name=name,mobile=mob,pin=pin,village=village,town=town,state=state)
            address.save()
            return redirect('/')
        else:
            return HttpResponse("404 page Error")    
    else:        
        fm=CustomerAddress()
        return render(request,"html/address-form.html",{"form":fm})
            
def set_default(request,id):
    Customer.objects.all().update(default=False)
    Customer.objects.filter(id=id).update(default=True) 
    return redirect('/address/')

def remove_address(reques,id):
    Customer.objects.filter(id=id).delete()
    return redirect("/address/")

def show_cart(request):
    total_cart=Cart.objects.all()
    default_address=Customer.objects.filter(default=True)
    params={'total_cart':total_cart,'default_address':default_address}
    return render(request,'html/show_cart.html',params)  

def remove_cart(request,id):
    Cart.objects.filter(id=id).delete()
    return redirect('/show_cart/')


def order_placed(request):
    order=Orderplaced.objects.all()
    return render(request,'html/order_placed.html',{'order':order})

def place_order(request,id):
    Customer_name=Customer.objects.get(default=True)
    product_name=Product.objects.get(id=id)
    buy_item=Orderplaced.objects.create(User=request.user,product=product_name,Customer=Customer_name,quantity=1)
    buy_item.save()
    return redirect('/order_placed/')           

def cancel_order(request,id):
    Orderplaced.objects.filter(id=id).delete()
    return redirect('/order_placed/')