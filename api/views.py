from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render
from requests import request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.

#Get all books
class GetBooksApiView(APIView):
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    filterset_fields = ['title','author']
    def get(self,request):
        qs=Book.objects.all()
        data=BookSerializer(qs,many=True).data
        return Response({'Books':data,'message':'Book are available'},status=200)

    def post(self,request):
        qs = BookSerializer(data=request.data)
        if qs.is_valid():
            qs.save()
            return Response({'message':'Book has posted'},status=201)
        return Response({'message':qs.errors})

    def delete(self,request,*args,**kwargs):
        user = request.user
        qs = Book.objects.get(id=self.kwargs.get('pk'))
        qs.delete()
        return Response({'message':'Book has deleted'})
#Get all orders
class OrderApiView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        qs=Order.objects.all().order_by('date_created')
        data=OrderSerializer(qs,many=True).data
        return Response({'Orders':data,'message':'Orders'},status=200)

    def post(self,request):
        qs = OrderSerializer(data=request.data)
        if qs.is_valid():
            qs.save()
            return Response({'message':'Orders Successfully'},status=200)
        return Response({'message':qs.errors},status=200)

    def delete(self,request,*args,**kwargs):
        user = request.user
        qs = Order.objects.get(user=user,id=self.kwargs.get('pk'))
        qs.delete()
        return Response({'msg':'deleted'})

#Get Most ordered books
class MostOrderAPIView(APIView):
    def get(self,request):
        qs = Order.objects.all().order_by('-quantity')
        data = OrderSerializer(qs,many=True).data
        return Response({'Orders by quantity':data,'message':'Most Orrdered'},status=200)
