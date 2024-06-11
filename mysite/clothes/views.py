from django.shortcuts import render
from clothes.models import Item

# Create your views here.
def home(request):
    items = Item.objects.all()
    productlist = Item.objects.filter(featured_product=True)

    context = {
        'items': items,
        'productlist': productlist
    }
    return render(request,'clothes/home.html', context)

def products(request):

    if request.user.is_superuser:
        itemlist = Item.objects.all()

        # for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains=item_name)
        

    elif request.user.is_authenticated and request.user.profile.user_type == 'com_owner':
        itemlist = Item.objects.filter(com_owner = request.user.id)
        
        # for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(com_owner = request.user.id, item_name__icontains=item_name)

    elif request.user.is_authenticated and request.user.profile.user_type == 'cust':
        itemlist = Item.objects.all()
        # for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains=item_name)


    else:
        itemlist = Item.objects.all()
                 # for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains=item_name)
    context = {
        'itemlist':itemlist
    }
    return render(request, 'clothes/products.html',context)
