from functools import partial
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductsSerializer
from .models import Products

# Create your views here.


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "list": "/product-list/",
        "detail_view": "/product-detail/<int:id>",
        "create": "/product-create",
        "update": "/product-update/<int:id>",
        "delete": "/product-delete/<int:id>",
    }
    return Response(api_urls)


@api_view(["GET"])
def showProducts(request):
    products = Products.objects.all()
    ser = ProductsSerializer(products, many=True)
    return Response(ser.data)


@api_view(["GET"])
def showProduct(request, pk):
    product = Products.objects.get(id=pk)
    ser = ProductsSerializer(product, many=False)
    return Response(ser.data)


@api_view(["POST"])
def createProduct(request):
    ser = ProductsSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)


@api_view(["PATCH"])
def updateProduct(request, pk):
    product = Products.objects.get(id=pk)
    if product:
        ser = ProductsSerializer(instance=product, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)
    else:
        return Response(product)


@api_view(["GET"])
def deleteProduct(request, pk):
    product = Products.objects.get(id=pk)
    if product:
        product.delete()
        return Response("Item deleted successfully")
    else:
        return Response("item not found")
