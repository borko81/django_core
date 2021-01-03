from django.shortcuts import render
from django.http import HttpResponse

from .forms import ProductForm
from .models import Product


def product_detail_view(request, pk):
    '''Show only one product'''
    obj = Product.objects.get(pk=pk)
    context = {
        'name': obj.name,
        'name_lat': obj.name_lat,
        'summary': obj.summary,
        'feuture': obj.feuture,
        'price': obj.price,
    }
    print(context)
    return render(request, 'message_and_list/product_detail_view.html', {'context': context})


# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()

#     context = {
#         'form': form
#     }
#     return render(request, 'message_and_list/add_new_product.html', context)

def product_create_view(request):
    '''Raw form create'''
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        name_lat = request.POST.get('name_lat')
        price = request.POST.get('price')
        summary = request.POST.get('summary')
        try:
            Product.objects.create(name=name, name_lat=name_lat, price=price, summary=summary)
        except:
            HttpResponse("Something wrong")
    return render(request, 'message_and_list/add_new_product.html', context)
