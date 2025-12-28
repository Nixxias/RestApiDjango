from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Author, Book, Copy
from .serializers import AuthorSerializer, BookSerializer, CopySerializer
from django.http import HttpResponse
from django.conf import settings
import os


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        author_id = self.request.query_params.get('authorId')
        if author_id is not None:
            queryset = queryset.filter(author__id=author_id)
        return queryset

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CopyViewSet(viewsets.ModelViewSet):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)

def serve_index(request):
    path = os.path.join(settings.BASE_DIR, 'index.html')
    with open(path, 'r', encoding='utf-8') as file:
        return HttpResponse(file.read())

def serve_main_js(request):
    path = os.path.join(settings.BASE_DIR, 'main.js')
    with open(path, 'r', encoding='utf-8') as file:
        return HttpResponse(file.read(), content_type='application/javascript')