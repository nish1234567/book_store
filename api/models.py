from operator import mod
from turtle import title
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CategoryBook(models.Model):
    bookcategory = models.CharField(max_length=200,null=True, default='CS')
    
    def __str__(self):
        return (self.bookcategory)
        
class Book(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(CategoryBook,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200,null=True)
    author = models.CharField(max_length=200,null=True)
    price = models.IntegerField()
    edition = models.IntegerField()

    def __str__(self):
        return str(self.title)

class Order(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     book = models.ForeignKey(Book, on_delete=models.PROTECT)
     date_created = models.DateTimeField(auto_now_add=True)
     quantity = models.IntegerField(null=True)

     def __str__(self):
         return str(self.book)