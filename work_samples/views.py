from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView
from .models import *
from .serializers import WorkSampleSerializer
# Create your views here.


class WorkSampleListApiView(ListAPIView):
    queryset = WorkSample.objects.all()
    serializer_class = WorkSampleSerializer


class WorkSampleRetrieveView(RetrieveAPIView):
    queryset = WorkSample.objects.all()
    serializer_class = WorkSampleSerializer
    lookup_field = 'slug'
