from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from library.models import newsmodel
from .serializers import NewsModelSerializer

class NewsModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = newsmodel.objects.all()
    serializer_class = NewsModelSerializer