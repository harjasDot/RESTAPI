from email import header
from django.shortcuts import render,redirect
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ApplySerializer

from .models import Apply

import requests
# Create your views here.

@api_view(['GET'])
def index(request):
    api_urls={
        'list':'http://127.0.0.1:8000/api/apply-list',
        'detail view':'http://127.0.0.1:8000/api/apply-detail/<str:pk>',
        'create':'http://127.0.0.1:8000/api/apply-create',
        'update':'http://127.0.0.1:8000/api/apply-update/<str:pk>',
        'delete':'http://127.0.0.1:8000/api/apply-delete/<str:pk>',
    }
    return Response(api_urls)

   


@api_view(['GET'])
def applyList(request):
    applications=Apply.objects.all()
    serialize=ApplySerializer(applications, many=True)
    return Response(serialize.data)

@api_view(['GET'])
def applyDetail(request,pk):
    applications=Apply.objects.get(id=pk)
    serialize=ApplySerializer(applications, many=False)
    return Response(serialize.data)

@api_view(['POST'])

def applyCreate(request):
    serialize=ApplySerializer(data=request.data)
    
    if serialize.is_valid():
        serialize.save()
    return redirect('apply-list')


@api_view(['DELETE'])
def applyDelete(request,pk):
    application=Apply.objects.get(id=pk)
    application.delete()
    return Response('Deleted successfully')

@api_view(['POST'])
def applyUpdate(request,pk):
    applications=Apply.objects.get(id=pk)
    serialize=ApplySerializer(data=request.data, instance=applications)
    if serialize.is_valid():
        serialize.save()
    return redirect('apply-list')