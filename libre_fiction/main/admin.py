from django.contrib import admin
from main.models import Book, Chapter, Like


class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1
    fields = ('order', 'title', 'content')
    ordering = ('order', 'created_at')
    readonly_fields = ('order',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published')
    list_filter = ('author', 'is_published')
    search_fields = ('title', 'author', 'description')
    list_editable = ('is_published',)
    inlines = (ChapterInline,)


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'book', 'created_at')
    list_filter = ('book',)
    search_fields = ('title', 'book', 'description')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'created_at')
    list_filter = ('user', 'book')
    search_fields = ('user', 'book')
