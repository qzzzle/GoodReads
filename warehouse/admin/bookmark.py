"""
Admin configuration for managing Bookmark instances.

This module customizes the admin interface for the Bookmark model,
enabling management of bookmark records.
"""

from django.contrib import admin

from ..models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    """
    Custom admin interface for Bookmark model.
    """

    list_display = ("user", "book", "created", "modified")
    list_filter = ("user", "book", "created", "modified")
    search_fields = ("user__username", "book__title")
    ordering = ("-created",)
    readonly_fields = ("created", "modified")

    fieldsets = (
        (None, {"fields": ("user", "book")}),
        (
            "Timestamps",
            {
                "fields": ("created", "modified"),
            },
        ),
    )
