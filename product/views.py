from django.shortcuts import render

from models.models import Product, ProductImage


def index(request):
    idproducts = request.GET.get('id')
    product = Product.objects.get(idproduct=idproducts)
    images = [p[1] for p in ProductImage.objects.filter(product=idproducts).values_list()]

    return render(request, 'index.html', {"product": product, "images": images})
