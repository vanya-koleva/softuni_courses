# Generated by Django 5.0.4 on 2025-02-19 11:59
import random

from django.db import migrations


def add_barcode(apps, schema_editor):
    Product = apps.get_model('main_app', 'Product')
    products = Product.objects.all()
    barcodes = random.sample(range(100000000, 1000000000), len(products))
    for i in range(len(products)):
        p = products[i]
        p.barcode = barcodes[i]
        p.save()

def remove_barcode(apps, schema_editor):
    Product = apps.get_model('main_app', 'Product')
    for p in Product.objects.all():
        p.barcode = 0
        p.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_product_barcode'),
    ]

    operations = [
        migrations.RunPython(add_barcode, reverse_code=remove_barcode),
    ]
