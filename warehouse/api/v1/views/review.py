"""
API views for submitting and updating reviews on books.
"""

import logging
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from warehouse.models import Book, Review
from ..serializers import ReviewSerializer

logger = logging.getLogger(__name__)


class SubmitReviewAPIView(APIView):
    """
    Handles the creation and updating of book reviews.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, book_id):
        """
        Create or fully update a review for a book.

        Scenario:
        - If the review exists, updates both rating and comment.
        - If the review doesn't exist, creates a new one.
        
        Logs the creation or update action.

        Returns:
        - 201 Created if a new review is created.
        - 200 OK if an existing review is updated.
        - 400 Bad Request if validation fails.
        - 500 Internal Server Error if an exception occurs.
        """
        try:
            book = get_object_or_404(Book, id=book_id)
            data = request.data.copy()
            data['book'] = book.id
            data['user'] = request.user.id

            serializer = ReviewSerializer(data=data)

            if serializer.is_valid():
                review, created = Review.objects.update_or_create(
                    user=request.user,
                    book=book,
                    defaults={
                        'rating': serializer.validated_data.get('rating'), 
                        'comment': serializer.validated_data.get('comment'),
                        }
                )

                if created:
                    logger.info(f"Review created for user {request.user.id} on book {book.id}")
                    return Response(
                        serializer.data,
                        status=status.HTTP_201_CREATED,
                    )
                
                logger.info(f"Review updated for user {request.user.id} on book {book.id}")
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,
                )

            logger.warning(f"Validation failed for review by user {request.user.id} on book {book.id}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        except Exception as e:
            logger.error(f"Error in creating/updating review for user {request.user.id} on book {book_id}: {str(e)}")
            return Response(
                {'error': 'An error occurred during the review process.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def patch(self, request, book_id):
        """
        Partially update an existing review for a book.

        Scenario:
        - Allows updating only the rating or comment without affecting the other field.
        
        Logs the update action.

        Returns:
        - 200 OK if the review is successfully updated.
        - 400 Bad Request if validation fails.
        - 404 Not Found if the review does not exist.
        - 500 Internal Server Error if an exception occurs.
        """
        try:
            review = get_object_or_404(Review, book_id=book_id, user=request.user)
            serializer = ReviewSerializer(review, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                logger.info(f"Review partially updated for user {request.user.id} on book {book_id}")
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK,
                    )
            
            logger.warning(f"Validation failed for user {request.user.id} on book {book_id}")
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
                )

        except Exception as e:
            logger.error(f"Error in partial update of review for user {request.user.id} on book {book_id}: {str(e)}")
            return Response(
                {'error': 'An error occurred during the review update process.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
