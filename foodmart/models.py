from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(blank=True)#upload_to = user_directory_path)
    quantity = models.IntegerField(blank=True, default=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_cart = models.BooleanField(default=False)

    @property
    def num_in_cart(self):
        return ShoppingCartItem.objects.get(item__id = self.id).quantity

    def __str__(self):
        return self.name


class ShoppingCartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.item.name + " - " + str(self.quantity)

    @property
    def cost(self):
        return self.quantity * self.item.price


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CategoryItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.name + " - " + self.item.name