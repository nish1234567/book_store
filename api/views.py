from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render
#from requests import request
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.

#Get all books
class GetBooksApiView(APIView):
    def get(self,request):
        permission_classes = [AllowAny] 
        qs=Book.objects.all()
        filter_backends = [SearchFilter]
        search_fields = ['title','author']
        data=BookSerializer(qs,many=True).data
        return Response({'Books':data,'message':'Book are available'},status=200)

    def post(self,request):
        permission_classes = [IsAuthenticated]
        qs = BookSerializer(data=request.data)
        if qs.is_valid():
            qs.save()
            return Response({'message':'Successfully'},status=200)
        return Response({'message':'Something went wrong'},status=200)

    def delete(self,request,pk):
        permission_classes = [IsAuthenticated]
        qs = Book.objects.get(id=pk)
        qs.delete()
        return Response({'Msg':'Order has canceled'})

'''class GetCategoryAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        #qs = Book.objects.select_related('category').all()
        qs = Book.objects.prefetch_related('category').all() 
        data = BookSerializer(qs,many=True).data
        return Response({'Category':data,'message':'Category'},status=200)'''

#Get all orders
class OrderApiView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        qs=Order.objects.all().order_by('date_created')
        #filter_backends = [OrderingFilter]
        #ordering_fields =['date_created']
        data=OrderSerializer(qs,many=True).data
        return Response({'Orders':data,'message':'Orders'},status=200)

    def post(self,request):
        qs = OrderSerializer(data=request.data)
        if qs.is_valid():
            qs.save()
            return Response({'message':'Orders Successfully'},status=200)
        return Response({'message':'Something went wrong'},status=200)

    def delete(self,request,pk):
        qs = Order.objects.get(id=pk)
        qs.delete()
        return Response({'Msg':'Order has canceled'})

#Get Most ordered books
class MostOrderAPIView(APIView):
    def get(self,request):
        qs = Order.objects.all().order_by('-quantity')
        data = OrderSerializer(qs,many=True).data
        return Response({'Orders by quantity':data,'message':'Most Orrdered'},status=200)