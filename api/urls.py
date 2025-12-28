
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, CopyViewSet, serve_index, serve_main_js


router = DefaultRouter(trailing_slash=False)
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')
router.register(r'copies', CopyViewSet, basename='copy')

urlpatterns = [

    path('', serve_index),           
    path('index.html', serve_index), 
    path('main.js', serve_main_js),  
] + router.urls