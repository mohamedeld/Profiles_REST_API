from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class HelloApiView(APIView):
    def get(self,request,format=None):
        an_apiview = [
            'Uses HTTP method as a function (get,post,patch,put,delete',
            'Is similar to a traditional django view',
            'Gives you the most control over your application logic',
            'is mapped manually to urls'
        ]
        
        return Response({'message':'hello world','an_apiview':an_apiview})
        