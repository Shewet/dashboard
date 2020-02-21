from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import action


# Create your views here.

# class productList(APIView):

#     def get(self,request):
#         products=Product.objects.all()
#         serializers=ProductSerializer(products,many=True)
#         return Response(serializers.data)





class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
