from django.contrib import admin
from ..models import Bookmark

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Bookmark instances.
    """
    list_display = ('user', 'book', 'created', 'modified')
    list_filter = ('user', 'book', 'created', 'modified')
    search_fields = ('user__username', 'book__title')
    ordering = ('-created',)
    readonly_fields = ('created', 'modified')
    fieldsets = (
        (None, {
            'fields': ('user', 'book')
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )
