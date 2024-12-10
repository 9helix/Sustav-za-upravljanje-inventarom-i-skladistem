# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import MyUser, Warehouse, Product, Inventory
from .forms import (
    UserRegistrationForm,
    UserLoginForm,
    WarehouseForm,
    ProductForm,
    InventoryForm,
)


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_admin = form.cleaned_data["is_admin"]
            user.save()
            return redirect("login")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


@login_required
def home(request):
    if request.user.is_admin:
        users = MyUser.objects.all()
        warehouses = Warehouse.objects.all()
        products = Product.objects.all()
        inventories = Inventory.objects.all()
        return render(
            request,
            "admin_home.html",
            {
                "users": users,
                "warehouses": warehouses,
                "products": products,
                "inventories": inventories,
            },
        )
    else:
        warehouses = Warehouse.objects.all()
        products = Product.objects.all()
        inventories = Inventory.objects.all()
        return render(
            request,
            "user_home.html",
            {
                "warehouses": warehouses,
                "products": products,
                "inventories": inventories,
            },
        )
