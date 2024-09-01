"""
Admin configuration for managing Review instances.

This module customizes the admin interface for the Review model,
enabling management of book reviews.
"""

from django.contrib import admin
from ..models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Custom admin interface for Review model.
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
