from django.contrib import admin

from catalog.models import Product, Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category',)
    # фильтрация
    list_filter = ('category',)
    # поиск
    search_fields = ('category', 'description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category',)
    # поиск
    search_fields = ('category',)