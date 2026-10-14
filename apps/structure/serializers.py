from rest_framework import serializers
from apps.structure.models import *

class AuthorSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"], required=True)
    class Meta:
        model = Author
        fields = ['id', 'full_name', 'birth_date']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'publication_date', 'available_copies']


class BooktoLoanSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'publication_date']


class LoanSerializer(serializers.ModelSerializer):
    book = BooktoLoanSerializer(read_only=True)
    class Meta:
        model = Loan
        fields = ['id', 'book', 'borrowed_at', 'returned_at']