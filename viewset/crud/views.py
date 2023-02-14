from django.shortcuts import render
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework import viewsets

# class CustomerViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer

class CustomerList(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdate(UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

