# factories.py
import factory
from faker import Faker
from .models import Warehouse, Product, Inventory

fake = Faker()


class WarehouseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Warehouse

    name = factory.LazyFunction(lambda: f"{fake.company()}")
    location = factory.Faker("address")
    capacity = factory.LazyFunction(lambda: fake.random_int(min=1000, max=10000))


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.LazyFunction(lambda: f"{fake.catch_phrase()}")
    description = factory.Faker("paragraph")
    price = factory.LazyFunction(lambda: fake.random_int(min=10, max=1000))
    sku = factory.Sequence(lambda n: f"{n:05d}")


class InventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Inventory

    warehouse = factory.SubFactory(WarehouseFactory)
    product = factory.SubFactory(ProductFactory)
    quantity = factory.LazyFunction(lambda: fake.random_int(min=0, max=1000))
