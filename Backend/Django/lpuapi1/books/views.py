from django.shortcuts import render
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer, CarSerializer
from .models import Car


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

# Create your views here.
