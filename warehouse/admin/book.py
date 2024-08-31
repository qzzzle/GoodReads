from django.contrib import admin
from ..models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Book instances.
    """
    list_display = ('title', 'author', 'created', 'modified')
    list_filter = ('author', 'created', 'modified')
    search_fields = ('title', 'author')
    ordering = ('-created',)
    readonly_fields = ('created', 'modified')
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'summary')
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )
