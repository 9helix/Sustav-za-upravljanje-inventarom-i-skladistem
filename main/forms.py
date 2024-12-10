# forms.py
from django import forms
from .models import MyUser, Warehouse, Product, Inventory


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ["email", "password", "is_admin"]


""" class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    is_admin = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = MyUser
        fields = ("email", "password1", "password2", "is_admin") """


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ["name", "location", "capacity"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "sku"]


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ["warehouse", "product", "quantity"]
