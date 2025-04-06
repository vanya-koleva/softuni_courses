from django import forms

from .models import Category, Fruit


class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'


class CategoryForm(CategoryBaseForm):
    pass


class FruitAddForm(FruitBaseForm):
    pass
