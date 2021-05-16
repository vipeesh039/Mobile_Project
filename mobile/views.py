from django.db.models import Sum
from django.shortcuts import render,redirect
from .forms import CreateProductForm
from .models import Product,Order,Carts
from .forms import UserRegistrationForm,LoginForm,OrderForm,CartForm,ChangePasswordForm
from django.contrib.auth import authenticate,login,logout
from .decorators import login_loginrequired,admin_only
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


# Create your views here.

@login_loginrequired
def base(request):
    return render(request,"mobile/base.html")


@login_loginrequired
def list_mobile(request):
    mobiles=Product.objects.all()
    context={}
    context["mobiles"]=mobiles
    return render(request,"mobile/listmobile.html",context)


@login_loginrequired
@admin_only
def add_product(request):
    form=CreateProductForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=CreateProductForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("base")
    return render(request,"mobile/createmobile.html",context)


def get_mobile_object(id):
    return Product.objects.get(id=id)

@login_loginrequired
def mobile_details(request,id):
    mobile=get_mobile_object(id)
    context={}
    context["mobile"]=mobile
    return render(request,"mobile/mobiledetails.html",context)
@login_loginrequired
@admin_only
def mobile_delete(request,id):
    mobile=get_mobile_object(id)
    mobile.delete()
    return redirect("listmobile")
@login_loginrequired
@admin_only
def mobile_update(request,id):
    mobile=get_mobile_object(id)
    form=CreateProductForm(instance=mobile)
    context={}
    context["form"]=form
    if request.method=='POST':
        form=CreateProductForm(instance=mobile,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("listmobile")
    return render(request,"mobile/mobileupdate.html",context)

def regstration(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"mobile/login.html")
        else:
            form=UserRegistrationForm(request.POST)
            context["form"]=form
            return redirect("userlogin")

    return render(request,"mobile/registration.html",context)

def login_user(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,"mobile/base.html")


    return render(request,"mobile/login.html",context)

def signout(request):
    logout(request)
    return redirect("userlogin")



@login_loginrequired
def item_order(request,id):
    product=get_mobile_object(id)
    form=OrderForm(initial={'user':request.user,'product':product})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listmobile")
        else:
            context["form"]=form
            return render(request, "mobile/ordereditem.html", context)
    return render(request,"mobile/ordereditem.html",context)

@login_loginrequired
def view_my_orders(request):
    orders=Order.objects.filter(user=request.user)
    context={}
    context["orders"]=orders
    return render(request,"mobile/vieworders.html",context)


@login_loginrequired
def order_cancel(request,id):
    order=Order.objects.get(id=id)
    order.status='cancelled'
    order.save()
    return redirect("vieworder")

@login_loginrequired
def add_to_cart(request,id):
    product = get_mobile_object(id)
    form = CartForm(initial={'user': request.user, 'product': product})
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listmobile")
        else:
            context["form"] = form
            return render(request, "mobile/mobiledetail.html", context)
    return render(request, "mobile/cartitem.html", context)

@login_loginrequired
def view_cart(request):
    cart_items=Carts.objects.filter(user=request.user)
    # context={}
    # context["cart_items"]=cart_items
    total=Carts.objects.filter(user=request.user).aggregate(Sum('price_total'))



    return render(request,"mobile/viewcart.html", {"cart_items":cart_items,"total":total})

@login_loginrequired
def remove_cart_item(request,id):
    item = Carts.objects.get(id=id)
    if item.qty > 1:
        item.qty -= 1
        item.save()
        return redirect("viewcart")
    else:
        item.delete()
        return redirect("viewcart")

@login_loginrequired
def item_order_cart(request,id):
    item = Carts.objects.get(id=id)
    form=OrderForm(initial={'user':request.user,'product':item.product})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            remove_cart_item(request,id=id)
            return redirect("viewcart")
        else:
            context["form"]=form
            return render(request, "mobile/ordereditem.html", context)
    return render(request,"mobile/ordereditem.html",context)

@login_loginrequired
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) #prevents from logging out after changing password
            messages.success(request, 'Your password was successfully updated!')
            return redirect('changepassword')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'mobile/changepassword.html', {
        'form': form
    })

@login_loginrequired
def admin_order_view(request):
    orders=Order.objects.all()
    context={}
    context["orders"]=orders
    return render(request,"mobile/viewordersadmin.html",context)

@login_loginrequired
def order_delivered(request,id):
    order=Order.objects.get(id=id)
    order.status='Delivered'
    order.save()
    return redirect("vieworderadmin")
@login_loginrequired
def order_shipped(request,id):
    order=Order.objects.get(id=id)
    order.status='Shipped'
    order.save()
    return redirect("vieworderadmin")