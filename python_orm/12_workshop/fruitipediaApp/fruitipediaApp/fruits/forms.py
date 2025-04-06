from django import forms

from .models import Category


class CategoryBaseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryForm(CategoryBaseForm):
    pass