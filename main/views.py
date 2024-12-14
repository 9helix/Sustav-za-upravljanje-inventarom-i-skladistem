# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import MyUser, Warehouse, Product, Inventory
from .forms import (
    InventoryFilterForm,
    ProductFilterForm,
    UserFilterForm,
    UserRegistrationForm,
    UserEditForm,
    UserLoginForm,
    WarehouseFilterForm,
    WarehouseForm,
    ProductForm,
    InventoryForm,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView


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
    return render(request, "home.html")


# views.py
class WarehouseListView(LoginRequiredMixin, ListView):
    model = Warehouse
    template_name = "warehouse_list.html"
    context_object_name = "warehouses"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        location = self.request.GET.get("location")

        if name:
            queryset = queryset.filter(name__icontains=name)
        if location:
            queryset = queryset.filter(location__icontains=location)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = WarehouseFilterForm(self.request.GET)
        return context


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")
        min_price = self.request.GET.get("min_price")

        if name:
            queryset = queryset.filter(name__icontains=name)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = ProductFilterForm(self.request.GET)
        return context


class InventoryListView(LoginRequiredMixin, ListView):
    model = Inventory
    template_name = "inventory_list.html"
    context_object_name = "inventories"

    def get_queryset(self):
        queryset = super().get_queryset()
        warehouse = self.request.GET.get("warehouse")
        product = self.request.GET.get("product")

        if warehouse:
            queryset = queryset.filter(warehouse=warehouse)
        if product:
            queryset = queryset.filter(product=product)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = InventoryFilterForm(self.request.GET)
        return context


class UserListView(LoginRequiredMixin, ListView):
    model = MyUser
    template_name = "user_list.html"
    context_object_name = "users"

    def get_queryset(self):
        queryset = super().get_queryset()
        email = self.request.GET.get("email")
        is_admin = self.request.GET.get("is_admin")

        if email:
            queryset = queryset.filter(email__icontains=email)
        if is_admin:
            queryset = queryset.filter(is_admin=True)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = UserFilterForm(self.request.GET)
        return context


@login_required
def add_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():

            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = form.save(commit=False)
            is_admin = form.cleaned_data["is_admin"]
            user = MyUser.objects.create_user(email, password, is_admin)
            user.save()
            return redirect("home")
    else:
        form = UserRegistrationForm()
    return render(request, "add_user.html", {"form": form})


@login_required
def edit_user(request, user_id):
    user = get_object_or_404(MyUser, id=user_id)
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserEditForm(instance=user)
    return render(request, "edit_user.html", {"form": form})


@login_required
def delete_user(request, user_id):
    user = get_object_or_404(MyUser, id=user_id)
    if request.method == "POST":
        user.delete()
        return redirect("home")
    return render(request, "delete_user.html", {"user": user})


@login_required
def add_warehouse(request):
    if request.method == "POST":
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = WarehouseForm()
    return render(request, "add_warehouse.html", {"form": form})


@login_required
def edit_warehouse(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, id=warehouse_id)
    if request.method == "POST":
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = WarehouseForm(instance=warehouse)
    return render(request, "edit_warehouse.html", {"form": form})


@login_required
def delete_warehouse(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, id=warehouse_id)
    if request.method == "POST":
        warehouse.delete()
        return redirect("home")
    return render(request, "delete_warehouse.html", {"warehouse": warehouse})


@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProductForm()
    return render(request, "add_product.html", {"form": form})


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProductForm(instance=product)
    return render(request, "edit_product.html", {"form": form})


@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect("home")
    return render(request, "delete_product.html", {"product": product})


@login_required
def add_inventory(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = InventoryForm()
    return render(request, "add_inventory.html", {"form": form})


@login_required
def edit_inventory(request, inventory_id):
    inventory = get_object_or_404(Inventory, id=inventory_id)
    if request.method == "POST":
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = InventoryForm(instance=inventory)
    return render(request, "edit_inventory.html", {"form": form})


@login_required
def delete_inventory(request, inventory_id):
    inventory = get_object_or_404(Inventory, id=inventory_id)
    if request.method == "POST":
        inventory.delete()
        return redirect("home")
    return render(request, "delete_inventory.html", {"inventory": inventory})


# views.py
from django.views.generic import DetailView


class UserDetailView(LoginRequiredMixin, DetailView):
    model = MyUser
    template_name = "user_detail.html"
    context_object_name = "user_detail"


class WarehouseDetailView(LoginRequiredMixin, DetailView):
    model = Warehouse
    template_name = "warehouse_detail.html"
    context_object_name = "warehouse"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inventories"] = Inventory.objects.filter(warehouse=self.object)
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inventories"] = Inventory.objects.filter(product=self.object)
        return context


class InventoryDetailView(LoginRequiredMixin, DetailView):
    model = Inventory
    template_name = "inventory_detail.html"
    context_object_name = "inventory"
