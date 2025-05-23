from django.core.exceptions import ValidationError


def validate_menu_categories(value):
    categories = ["Appetizers", "Main Course", "Desserts"]
    for category in categories:
        if category not in value:
            raise ValidationError(f'The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')
