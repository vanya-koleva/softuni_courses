from django.contrib import admin

from books_api.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    ...
