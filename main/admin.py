from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug'] # list display - параметры из models.Category которые будут отображаться в админке
    prepopulated_fields = {'slug': ('name',)} # это поля, которые будут заполнены автоматически

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created', 'updated']
    list_filter = ['category', 'available', 'updated', 'created'] # как можно фильтровать товары в АДМИНКЕ
    list_editable = ['price', 'available'] # параметры, которые можно менять
    prepopulated_fields = {'slug': ('name',)}
