import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Product, Order


def populate_db() -> None:
    profile1 = Profile(
        full_name='Adam Smith',
        email='adam.smith@example.com',
        phone_number='123456789',
        address='123 Main St, Springfield',
        is_active=True,
    )
    profile2 = Profile(
        full_name='Susan James',
        email='adam.smith@example.com',
        phone_number='123456789',
        address='123 Main St, Springfield',
        is_active=True,
    )

    profile1.save()
    profile2.save()

    product1 = Product(
        name='Desk M',
        description='A medium-sized office desk',
        price=150,
        in_stock=10,
        is_available=True,
    )
    product2 = Product(
        name='Display DL',
        description='A 24-inch HD display',
        price=200,
        in_stock=5,
        is_available=True,
    )

    product1.save()
    product2.save()

    order1 = Order(
        profile=profile1,
        total_price=150,
        is_completed=False,
    )
    order1.save()
    order1.products.add(product1)

    order2 = Order(
        profile=profile2,
        total_price=200,
        is_completed=True,
    )
    order2.save()
    order2.products.add(product2)
