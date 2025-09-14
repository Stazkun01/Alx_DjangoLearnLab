from django.contrib import admin
from .models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # show these fields in list view
    search_fields = ('title', 'author')                     # search by title or author
    list_filter = ('publication_year',)                     # filter by year

# Register the Book model with custom admin
admin.site.register(Book, BookAdmin)
