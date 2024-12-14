# forms.py
from django import forms
from .models import MyUser, Warehouse, Product, Inventory


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ["email", "password", "is_admin"]


class UserEditForm(forms.ModelForm):
    email = forms.EmailField()
    is_admin = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = MyUser
        fields = ("email", "is_admin")


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


class WarehouseFilterForm(forms.Form):
    name = forms.CharField(required=False)
    location = forms.CharField(required=False)


class ProductFilterForm(forms.Form):
    name = forms.CharField(required=False)
    min_price = forms.DecimalField(required=False)


class InventoryFilterForm(forms.Form):
    warehouse = forms.ModelChoiceField(queryset=Warehouse.objects.all(), required=False)
    product = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)


class UserFilterForm(forms.Form):
    email = forms.CharField(required=False)
    is_admin = forms.BooleanField(required=False)
