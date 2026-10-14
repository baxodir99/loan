from django.urls import path
from rest_framework.views import APIView, Response
from .models import Book, Loan
from apps.user.models import Author
from .serializers import AuthorSerializer, BookSerializer, LoanSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend

class AuthorAPIView(APIView):
    permission_classes = [AllowAny]  # Allow any user to access this view
    authentication_classes = []  # Disable authentication for this view
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

        
class BookAPIView(APIView):
    permission_classes = [AllowAny]  # Allow any user to access this view
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']
    search_fields = ['title']
    ordering_fields = ['publication_date']
    

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class AuthorCreateUpdateDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response({"error": "Author not found"}, status=404)

        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response({"error": "Author not found"}, status=404)

        author.delete()
        return Response(status=204)


class BookCreateUpdateDeleteAPIView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=404)

        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=404)

        book.delete()
        return Response(status=204)


class BookBorrowAPIView(APIView):

    def post(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=404)

        if book.available_copies <= 0:
            return Response({"error": "All books are currently borrowed."}, status=400)

        # Create a loan record
        loan = Loan.objects.create(book=book, user=request.user)
        book.available_copies -= 1
        book.save()

        return Response({"message": f"You have borrowed '{book.title}'."}, status=200)


class BookReturnAPIView(APIView):

    def post(self, request, pk):
        try:
            loan = Loan.objects.get(id=pk, user=request.user)
        except Loan.DoesNotExist:
            return Response({"error": "Loan record not found or already returned"}, status=404)

        loan.returned_at = timezone.now()
        loan.save()

        book = Loan.objects.get(id=pk).book
        book.available_copies += 1
        book.save()

        return Response({"message": f"You have returned '{book.title}'."}, status=200)


class LoanAPIView(APIView):
    def get(self, request):
        loans = Loan.objects.filter(user=request.user)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)