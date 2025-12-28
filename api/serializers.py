from rest_framework import serializers
from .models import Author, Book, Copy

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name']
    
    def validate_first_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("First name cannot be empty.")
        return value

    def validate_last_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Last name cannot be empty.")
        return value

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    
    authorId = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), 
        source='author', 
        write_only=True
    )

    class Meta:
        model = Book
        fields = ['id', 'title', 'year', 'author', 'authorId']

    def validate_year(self, value):
        if value < 0:
            raise serializers.ValidationError("Year cannot be negative.")
        return value
    
    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty.")
        return value

class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ['id', 'book', 'inventory_number']