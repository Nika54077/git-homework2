from django.contrib import admin
from .models import Author, Book, Review

class ReviewInLine(admin.TabularInline):
    model = Review
    extra = 1

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating')
    search_fields = ('name',)
    ordering = ("-rating",)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'price')
    list_filter = ('genre', 'published_date')
    autocomplete_fields = ['author']
    inlines = [ReviewInLine]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review)

