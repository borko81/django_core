from django.shortcuts import render

from .models import Product


def product_detail_view(request):
    '''Show only one product'''
    obj = Product.objects.get(id=1)
    context = {
        'name': obj.name,
        'name_lat': obj.name_lat,
        'summary': obj.summary,
        'feuture': obj.feuture,
        'price': obj.price,
    }
    print(context)
    return render(request, 'message_and_list/product_detail_view.html', {'context': context})
