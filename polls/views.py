from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from oauth2_provider.views.generic import ProtectedResourceView
from rest_framework import generics
from .models import Customer
from .serializers import *

@login_required
def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

class MyProtectedEndPoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, there!!')

class SubjectListView(generics.ListAPIView):
	queryset = Customer.objects.all()
	serializer_class = AccountSerializer

class SubjectDetailView(generics.RetrieveAPIView):
	queryset = Customer.objects.all()
	serializer_class = AccountSerializer