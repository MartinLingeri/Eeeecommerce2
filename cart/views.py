from django.shortcuts import render, redirect
from django.http import JsonResponse

from models.models import Cart, Product, CartProduct

import mercadopago
from .cfgMP import prod_access_token, test_access_token

sdk = mercadopago.SDK(test_access_token)

back_urls = {
    "success": "http://localhost:8000/purcahses",
    "failure": "http://localhost:8000/failure",
    "pending": "http://localhost:8000/pending"
}

preference_data = {
    "items": [
        {
            "id": 1,
            "title": "Mi producto",
            "quantity": 1,
            "currency_id": "ARS",
            "unit_price": 1,
        }
    ],
    "back_urls": back_urls,
}

preference_response = sdk.preference().create(preference_data)
preference_id = preference_response["response"]["id"]


def index(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    idcart = Cart.objects.get(user=request.user.id).idcart
    cart = CartProduct.objects.filter(cart=idcart).values_list()
    products = getProducts(request)

    updatePreference(products)

    return render(request, "cart.html", {"cart": cart, "products": products, "preference_id": preference_id})


def add(request, id, quantity):
    if not request.user.is_authenticated:
        return redirect('/login')

    idcart = Cart.objects.get(user=request.user.id).idcart
    product = Product.objects.get(idproduct=id)
    cart = CartProduct.objects.filter(cart=idcart, product=product.idproduct)
    if cart:
        cart = cart[0]
        cart.quantity = min(quantity, 9)
        try:
            cart.save()
        except:
            return JsonResponse({"status": "notok"})
    else:
        cart = CartProduct.objects.create(
            cart=idcart, product=product.idproduct, quantity=quantity)


    products = getProducts(request)

    updatePreference(products)

    return JsonResponse({"status": "ok"})


def remove(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')

    idcart = Cart.objects.get(user=request.user.id).idcart
    cart = CartProduct.objects.get(cart=idcart, product=id)
    cart.delete()

    products = getProducts(request)

    updatePreference(products)

    return JsonResponse({"status": "ok"})


def getProducts(request):
    idcart = Cart.objects.get(user=request.user.id).idcart
    cart = CartProduct.objects.filter(cart=idcart).values_list()
    products = []
    for product in cart:
        product_raw = Product.objects.filter(
            idproduct=product[2]).values_list()[0]
        products.append({"name": product_raw[1], "price": product_raw[3],
                        "total": product_raw[3]*product[3], "quantity": product[3], "id": product_raw[0]})

    return products


def updatePreference(products):
    items = []
    for i in range(len(products)):
        item = {
            "id": products[i]["id"],
            "title": products[i]["name"],
            "quantity": products[i]["quantity"],
            "unit_price": products[i]["price"],
            "currency_id": "ARS",
        }
        items.append(item)
    
    preference_data = {
        "items": items,
        "back_urls": back_urls,
    }

    sdk.preference().update(preference_id, preference_data)

def purchase(request):
    pass