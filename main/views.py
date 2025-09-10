from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None): # cat_slug это парамеры запроса по фильтрации, в начале никак не надо фильтровать поэтому None
    categories = Category.objects.all() # достаём все категории из бд
    products = Product.objects.filter(available=True)
    
    category = None

    if category_slug:
        category = get_object_or_404(Category, category_slug=category_slug) # получаем категории из бд по category_slug
        products = products.filter(category=category)
    
    return render(request, 'main/product/list.html', 
                {
                    'category': category,
                    'categories': categories,
                    'products': products
                })
    
    