from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductsSerializer
from .models import Products

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls= {
        'list':'/product-list/',
        'detail_view':'/product-detail/<int:id>',
        'create':'/product-create',
        'update':'/product-update/<int:id>',
        'delete':'/product-delete/<int:id>',
    }
    return Response(api_urls)

@api_view(['GET'])
def showProducts(request):
    products = Products.objects.all()
    ser = ProductsSerializer(products, many=True)
    return Response(ser.data)
