from django.contrib import admin
from .models import Item, ShoppingCartItem, Category, CategoryItem

# Register your models here.
admin.site.register(Item)
admin.site.register(ShoppingCartItem)
admin.site.register(Category)
admin.site.register(CategoryItem)