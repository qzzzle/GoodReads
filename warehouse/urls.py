"""urls"""
from django.urls import path

from rest_framework.routers import DefaultRouter

from .api.v1.views import (
    BookListAPIView,
    BookDetailAPIView,
    BookmarkAPIView,
    SubmitReviewAPIView,
)


router = DefaultRouter()
urlpatterns = router.urls

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book-list'),
    path('<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('<int:book_id>/bookmark/', BookmarkAPIView.as_view(), name='bookmark'),
    path('<int:book_id>/review/', SubmitReviewAPIView.as_view(), name='submit-review'),
]

