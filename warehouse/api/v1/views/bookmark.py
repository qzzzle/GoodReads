"""
This module defines the API for managing bookmarks on books.
"""

import logging
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from warehouse.models import Book, Review, Bookmark

logger = logging.getLogger(__name__)

class BookmarkAPIView(APIView):
    """
    Handles bookmarking and unbookmarking of books by users.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, book_id):
        """
        POST: Bookmark a book or remove an existing bookmark.
        
        - If the user has bookmarked the book, the bookmark is removed.
        - If the user has reviewed/rated the book, bookmarking is blocked.
        - If the book isn't bookmarked and not reviewed, a new bookmark is created.
        
        Returns a message indicating the action performed.
        """
        try:
            book = get_object_or_404(Book, id=book_id)

            bookmark = Bookmark.objects.filter(user=request.user, book=book).first()

            if bookmark:
                bookmark.delete()
                logger.info(f"Bookmark removed for user {request.user.id} on book {book.id}")
                return Response(
                    {'message': 'Bookmark removed'},
                    status=status.HTTP_204_NO_CONTENT,
                )

            if Review.objects.filter(user=request.user, book=book).exists():
                logger.warning(f"User {request.user.id} attempted to bookmark a reviewed/rated book {book.id}")
                return Response(
                    {'error': 'Cannot bookmark a book you have reviewed or rated'},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            Bookmark.objects.create(user=request.user, book=book)
            logger.info(f"Bookmark created for user {request.user.id} on book {book.id}")
            return Response(
                {'message': 'Book bookmarked'},
                status=status.HTTP_201_CREATED,
            )

        except Exception as e:
            logger.error(f"Error in bookmarking/unbookmarking process for user {request.user.id} on book {book_id}: {str(e)}")
            return Response(
                {'error': 'An error occurred during the bookmarking process.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
