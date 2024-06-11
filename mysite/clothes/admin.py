from django.contrib import admin
from clothes.models import Item
from clothes.models import Category


# Register your models here.
admin.site.register(Item)
admin.site.register(Category)