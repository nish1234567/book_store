from rest_framework.serializers import *
from .models import *

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'