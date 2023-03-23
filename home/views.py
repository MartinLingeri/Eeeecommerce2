from django.shortcuts import render

from models.models import Product, ProductImage

def index(request):
    productos = []

    for p in Product.objects.all().values_list():
        productsImages = [i[1] for i in ProductImage.objects.filter(product=p[0]).values_list()]
        productos.append(
            dict({"idproducts": p[0], "name": p[1], "description": p[2], "price": p[3], "images": productsImages}))

    return render(request, "home/index.html", {"products": productos})
