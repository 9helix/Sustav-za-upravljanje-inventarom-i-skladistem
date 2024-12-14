"""
URL configuration for lab4 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from main.views import (
    InventoryListView,
    ProductListView,
    UserListView,
    WarehouseListView,
    register,
    user_login,
    user_logout,
    home,
    add_user,
    edit_user,
    delete_user,
    add_warehouse,
    edit_warehouse,
    delete_warehouse,
    add_product,
    edit_product,
    delete_product,
    add_inventory,
    edit_inventory,
    delete_inventory,
)

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("add_user/", add_user, name="add_user"),
    path("edit_user/<int:user_id>/", edit_user, name="edit_user"),
    path("delete_user/<int:user_id>/", delete_user, name="delete_user"),
    path("add_warehouse/", add_warehouse, name="add_warehouse"),
    path("edit_warehouse/<int:warehouse_id>/", edit_warehouse, name="edit_warehouse"),
    path(
        "delete_warehouse/<int:warehouse_id>/",
        delete_warehouse,
        name="delete_warehouse",
    ),
    path("add_product/", add_product, name="add_product"),
    path("edit_product/<int:product_id>/", edit_product, name="edit_product"),
    path("delete_product/<int:product_id>/", delete_product, name="delete_product"),
    path("add_inventory/", add_inventory, name="add_inventory"),
    path("edit_inventory/<int:inventory_id>/", edit_inventory, name="edit_inventory"),
    path(
        "delete_inventory/<int:inventory_id>/",
        delete_inventory,
        name="delete_inventory",
    ),
    path("warehouses/", WarehouseListView.as_view(), name="warehouse_list"),
    path("products/", ProductListView.as_view(), name="product_list"),
    path("inventories/", InventoryListView.as_view(), name="inventory_list"),
    path("users/", UserListView.as_view(), name="user_list"),
]
