from django.forms import ModelForm
from .models import Product,Order,Carts
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
class CreateProductForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","password1","password2","email"]


class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()



class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=["address","product","user"]
        widgets = {
            'address': forms.TextInput(attrs={'class': 'text_inp'}),
            'product': forms.Select(attrs={'class': 'text_inp'}),
            'user': forms.TextInput(attrs={'class': 'text_inp'}),

        }
        labels = {
            'user':'Username'
        }




class CartForm(ModelForm):
    class Meta:
        model = Carts
        fields="__all__"
        widgets = {
           'product': forms.Select(attrs={'class': 'text_inp'}),
            'qty': forms.NumberInput(attrs={'class': 'text_inp'}),
            'user': forms.TextInput(attrs={'class': 'text_inp'}),
        }
        labels = {
            'qty':'Quantity',
            'user': 'Username'
        }



class ChangePasswordForm(PasswordChangeForm):
    class Meta:
        widgets = {
            'old_password': forms.PasswordInput(attrs={'class': 'text_inp'}),
            'new_password1': forms.PasswordInput(attrs={'class': 'text_inp'}),
            'new_password2': forms.PasswordInput(attrs={'class': 'text_inp'})
    }