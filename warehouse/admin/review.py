from django.contrib import admin
from ..models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Review instances.
    """
    list_display = ('user', 'book', 'rating', 'created', 'modified')
    list_filter = ('rating', 'created', 'modified')
    search_fields = ('user__username', 'book__title', 'comment')
    ordering = ('-created',)
    readonly_fields = ('created', 'modified')
    fieldsets = (
        (None, {
            'fields': ('user', 'book', 'rating', 'comment')
        }),
        ('Timestamps', {
            'fields': ('created', 'modified'),
        }),
    )
