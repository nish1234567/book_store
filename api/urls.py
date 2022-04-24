from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('books_list',GetBooksApiView.as_view()),
    path('order_list',OrderApiView.as_view()),
    #path('search_books',SearchingAPIView.as_view())
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tokenrefresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('most_order',MostOrderAPIView.as_view()),
    #path('category',GetCategoryAPIView.as_view())
]
