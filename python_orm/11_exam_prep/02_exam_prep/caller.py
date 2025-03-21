import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Product, Order
from django.db.models.query_utils import Q


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

def get_profiles(search_string=None) -> str:
    if search_string is None:
        return ""

    profiles = Profile.objects.filter(
        Q(full_name__icontains=search_string)
        |
        Q(email__icontains=search_string)
        |
        Q(phone_number__icontains=search_string)
    ).order_by('full_name')

    if not profiles:
        return ""

    return "\n".join(
        f"Profile: {p.full_name},"
        f" email: {p.email}, phone number: {p.phone_number},"
        f" orders: {p.order_set.count()}"
        for p in profiles
    )

def get_loyal_profiles() -> str:
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ""

    return "\n".join(
        f"Profile: {p.full_name}, orders: {p.orders_count}"
        for p in profiles
    )

def get_last_sold_products() -> str:
    last_order = Order.objects.prefetch_related('products').last()

    if not last_order or not last_order.products.exists():
        return ""

    products_names = [p.name for p in last_order.products.all()]

    return f"Last sold products: {', '.join(products_names)}"
