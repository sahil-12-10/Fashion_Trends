from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.category_name
    
class Item(models.Model):
    com_owner = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        default = 1
    )
    prod_code = models.IntegerField(default = 50)
    for_user = models.CharField(
        max_length = 100,
        default = 'ClothOwner'
    )
    item_name = models.CharField(max_length = 100)
    item_desc = models.CharField(max_length = 500)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length = 1000,
        default = 'https://th.bing.com/th/id/OIP.rg_dE8HiSUNjMwZHNHz_8AHaHa?rs=1&pid=ImgDetMain'
    )
    item_category = models.ForeignKey(Category,on_delete = models.CASCADE, default=1)
    featured_product = models.BooleanField(default = False)

    def __str__(self):
        return self.item_name
