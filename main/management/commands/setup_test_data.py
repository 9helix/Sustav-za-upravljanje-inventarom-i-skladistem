# Create test data
from main.factories import InventoryFactory, ProductFactory, WarehouseFactory
from main.models import Inventory, Product, Warehouse

warehouse = WarehouseFactory()
product = ProductFactory()
inventory = InventoryFactory(warehouse=warehouse, product=product)


from django.db import transaction
from django.core.management.base import BaseCommand


NUM_WAREHOUSES = 5
NUM_PRODUCTS = 10
NUM_INVENTORIES = 15


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Warehouse, Product, Inventory]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        warehouses = WarehouseFactory.create_batch(5)
        products = ProductFactory.create_batch(10)
        inventories = InventoryFactory.create_batch(15)
