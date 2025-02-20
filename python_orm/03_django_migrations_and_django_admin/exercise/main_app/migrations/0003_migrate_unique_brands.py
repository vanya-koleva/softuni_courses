# Generated by Django 5.0.4 on 2025-02-20 07:38

from django.db import migrations


def create_unique_brands(apps, schema_editor):
    ShoeModel = apps.get_model('main_app', 'Shoe')
    UniqueBrands = apps.get_model('main_app', 'UniqueBrands')

    unique_brands = ShoeModel.objects.values_list('brand', flat=True).distinct()
    unique_brands_to_create = [UniqueBrands(brand_name=brand_name) for brand_name in unique_brands]

    UniqueBrands.objects.bulk_create(unique_brands_to_create)

def delete_unique_brands_data(apps, schema_editor):
    UniqueBrands = apps.get_model('main_app', 'UniqueBrands')
    UniqueBrands.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_uniquebrands'),
    ]

    operations = [
        migrations.RunPython(create_unique_brands, reverse_code=delete_unique_brands_data),
    ]
