from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer
from rest_framework import viewsets
# Create your views here.
class HelloApiView(APIView):
    serializer_class = HelloSerializer
    
    def get(self,request,format=None):
        an_apiview = [
            'Uses HTTP method as a function (get,post,patch,put,delete',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'is mapped manually to urls'
        ]
        
        return Response({'message':'hello world','an_apiview':an_apiview})
        
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )
        
    def put(self,request,pk=None):
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})
        
    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})
        
class HelloViewSet(viewsets.ViewSet):
    serializer_class = HelloSerializer
    
    def list(self,request):
        a_viewsets=[
            'Uses action (list, create,retrieve,update,partial_update)',
            'Automatically maps to urls using routers',
            'Provides more functionality with less code',
        ]
        return Response({'message':'hello','a_viewsets':a_viewsets})
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
            
    def retrieve(self,request,pk=None):
        return Response({'http_method':'GET'})
    
    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})
        
    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})
        
    def destory(self,request,pk=None):
        return Response({'http_method':'DELETE'})