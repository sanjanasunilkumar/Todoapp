from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from todoapp.models import Products
from todoapp.serializers import ProductSerializer
# Create your views here.

# it contains list() create() retrive() update() destroy()
class ProductsView(ViewSet):

    def list(self,request,*args, **kwargs):
        qs=Products.objects.all()
        serializer=ProductSerializer(qs,many=True)
        return Response(data=serializer.data)

    def create(self,request,*args, **kwargs):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            Products.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(serializer.errors)

    def retrieve(self,request,*args, **kwargs):
        id=kwargs.get("pk")
        qs=Products.objects.get(id=id)
        serializer=ProductSerializer(qs)
        return Response(data=serializer.data)
    
    def update(self,request,*args, **kwargs):
        return Response(data="updating a products")

    def destroy(self,request,*args, **kwargs):
        return Response(data="deleted")