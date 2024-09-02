"""
API views for listing and retrieving book details.

Provides API endpoints for listing all books and retrieving detailed information about a
specific book.
"""

import logging

from rest_framework import generics, permissions

from warehouse.models import Book

from ..serializers import BookDetailSerializer, BookSerializer


logger = logging.getLogger(__name__)


class BookListAPIView(generics.ListAPIView):
    """
    API view to list all books.

    - Accessible to authenticated users and read-only for others.
    - Uses BookSerializer to serialize book data.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            logger.error("Error in listing books: %s", str(e))
            raise


class BookDetailAPIView(generics.RetrieveAPIView):
    """
    API view to retrieve detailed information about a specific book.

    - Accessible to authenticated users and read-only for others.
    - Uses BookDetailSerializer to serialize detailed book data.
    """

    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Exception as e:
            logger.error(
                "Error in retrieving book details for book id %s: %s",
                kwargs.get("pk"),
                str(e),
            )
            raise
