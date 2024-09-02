"""
Admin configuration for managing Book instances.

This module customizes the admin interface for the Book model, enabling management of
book records.
"""

from django.contrib import admin

from ..models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Custom admin interface for Book model.
    """

    list_display = ("title", "created", "modified")
    list_filter = ("created", "modified")
    search_fields = ("title",)
    ordering = ("-created",)
    readonly_fields = ("created", "modified")

    fieldsets = (
        (None, {"fields": ("title", "summary")}),
        (
            "Timestamps",
            {
                "fields": ("created", "modified"),
            },
        ),
    )
