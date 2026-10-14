from django.contrib import admin
from .models import Book, Loan

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'publication_date', 'available_copies')
    search_fields = ('title', 'author__full_name', 'isbn')
    list_filter = ('publication_date',)

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'borrowed_at', 'returned_at')
    search_fields = ('book__title', 'user__username')
    list_filter = ('borrowed_at', 'returned_at')
