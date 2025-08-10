from django.shortcuts import render, redirect
from .models import Item, ShoppingCartItem, Category, CategoryItem


def home(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        id_of_item = int(request.POST.get('id_of_item'))

        if action == 'put':
            item = Item.objects.get(pk=id_of_item)
            item.in_cart = True
            item.save()
            if ShoppingCartItem.objects.filter(item=item).exists():
                cart_item = ShoppingCartItem.objects.get(item=item)
                cart_item.quantity += 1
                cart_item.save()
            else:
                shopping_cart_item = ShoppingCartItem(item=item, quantity=1)

                shopping_cart_item.save()

            return redirect("/")

    context = {
        'items': Item.objects.all(),
        'categories': Category.objects.all(),
        'page': "home"
    }

    return render(request, 'foodmart/home.html', context)


def cart(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        id_of_item = int(request.POST.get('id_of_item'))
        item = ShoppingCartItem.objects.get(pk=id_of_item)
        if action == 'increment':
            item.quantity += 1
            item.save()

        elif action == 'decrement':
            if item.quantity > 1:
                item.quantity -= 1
            item.save()
        elif action == 'delete':
            food_item = item.item
            food_item.in_cart = False
            food_item.save()

            item.delete()

        return redirect("/cart")

    context = {
        'items': ShoppingCartItem.objects.all(),
        'categories': Category.objects.all(),
        'page': "cart",
        'total_cost': sum(obj.cost for obj in ShoppingCartItem.objects.all()),
        'num_instances': ShoppingCartItem.objects.all().count()
    }

    return render(request, 'foodmart/cart.html', context)


def category(request, categoryname):
    if request.method == 'POST':
        action = request.POST.get('action')
        id_of_item = int(request.POST.get('id_of_item'))

        if action == 'put':
            item = Item.objects.get(pk=id_of_item)
            item.in_cart = True
            item.save()
            if ShoppingCartItem.objects.filter(item=item).exists():
                cart_item = ShoppingCartItem.objects.get(item=item)
                cart_item.quantity += 1
                cart_item.save()
            else:
                shopping_cart_item = ShoppingCartItem(item=item, quantity=1)

                shopping_cart_item.save()

            return redirect("/category/" + categoryname)

    # we get all the items that belong to the category
    items = CategoryItem.objects.filter(category__name=categoryname)

    # put the primary keys of all the items returned from prev query into a  list
    item_ids = items.values_list('item_id', flat=True)

    context = {
        'items': Item.objects.filter(id__in=item_ids),
        'categories': Category.objects.all(),
        'page': "aisles",
        'category_name': categoryname,
    }

    return render(request, 'foodmart/category.html', context)


def item(request, pk):
    if request.method == 'POST':
        action = request.POST.get('action')
        id_of_item = int(request.POST.get('id_of_item'))

        if action == 'put':
            item = Item.objects.get(pk=id_of_item)
            item.in_cart = True
            item.save()
            if ShoppingCartItem.objects.filter(item=item).exists():
                cart_item = ShoppingCartItem.objects.get(item=item)
                cart_item.quantity += 1
                cart_item.save()
            else:
                shopping_cart_item = ShoppingCartItem(item=item, quantity=1)

                shopping_cart_item.save()

            return redirect("/item/" + str(id_of_item))

    item = Item.objects.get(pk=pk)
    context = {
        'item': item,
        'categories': Category.objects.all(),
    }

    return render(request, 'foodmart/item.html', context)

