"""mobileproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .views import base,list_mobile,add_product,mobile_details,mobile_update,mobile_delete,regstration,login_user,signout,item_order,view_my_orders,order_cancel,add_to_cart,view_cart,remove_cart_item,change_password,item_order_cart,admin_order_view,order_shipped,order_delivered


urlpatterns = [
    path('',base,name="base"),
    path('mobiles',list_mobile,name="listmobile"),
    path('add',add_product,name="addproduct"),
    path('details/<int:id>',mobile_details,name="mdetails"),
    path('update/<int:id>',mobile_update,name="mupdate"),
    path('delete/<int:id>',mobile_delete,name="mdelete"),
    path('reg',regstration,name="registration"),
    path('login',login_user,name="userlogin"),
    path('logout',signout,name="signout"),
    path("itemorderd/<int:id>",item_order,name="order"),
    path("vieworder",view_my_orders,name="vieworder"),
    path("cancelorder/<int:id>",order_cancel,name="cancel_order"),
    path("addtocart/<int:id>",add_to_cart,name="addtocart"),
    path("viewcart",view_cart,name="viewcart"),
    path("removeitem/<int:id>",remove_cart_item,name="removeitem"),
    path("changepassword",change_password,name="changepassword"),
    path("itemorderdcart/<int:id>",item_order_cart,name="cartorder"),
    path("adminvieworder",admin_order_view,name="vieworderadmin"),
    path("deliveredorder/<int:id>",order_delivered,name="orderdelivered"),
    path("shiporder/<int:id>",order_shipped,name="ordership"),
]
