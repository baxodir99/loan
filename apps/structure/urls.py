from django.urls import path, include
from .views import AuthorAPIView, BookAPIView, BookCreateUpdateDeleteAPIView, AuthorCreateUpdateDeleteAPIView, BookBorrowAPIView, BookReturnAPIView, LoanAPIView



app_name = "structure-api"

urlpatterns = [
    path("authors/", AuthorAPIView.as_view(), name="authors-list"),
    path("books/", BookAPIView.as_view(), name="books-list"),
    path("admin/authors/", AuthorCreateUpdateDeleteAPIView.as_view(), name="author-create"),
    path("admin/books/", BookCreateUpdateDeleteAPIView.as_view(), name="book-create"),

    path("books/<int:pk>/borrow/", BookBorrowAPIView.as_view(), name="book-borrow"),
    path("books/<int:pk>/return/", BookReturnAPIView.as_view(), name="book-return"),
    path("loans/", LoanAPIView.as_view(), name="loans-list"),
]