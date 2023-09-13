from django.shortcuts import render
from .models import Category, drugItem
from .serializers import CategorySerilizers, drugItemSerilizers
from rest_framework import generics

# Create your views here.

# creating category views
class categoryViews(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerilizers


# creating drug items views 
class drugItemsViews(generics.ListCreateAPIView):
    queryset = drugItem.objects.all()
    serializer_class = drugItemSerilizers
    ordering_fields = ["price", "inStock"]
    filterset_fields  = ["price", "inStock"]
    search_fields  = ["name"]


# creating single drug item views
class singleDrugItemViews(generics.ListCreateAPIView):
    queryset = drugItem.objects.all()
    serializer_class = drugItemSerilizers