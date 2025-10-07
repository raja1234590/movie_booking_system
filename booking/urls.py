# booking/urls.py
from django.urls import path
from .views import (
    SignupView, MovieListView, MovieShowsListView,
    ShowBookAPIView, BookingCancelAPIView, MyBookingsListView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # returns access + refresh
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('movies/', MovieListView.as_view(), name='movies-list'),
    path('movies/<int:movie_id>/shows/', MovieShowsListView.as_view(), name='movie-shows'),
    path('shows/<int:show_id>/book/', ShowBookAPIView.as_view(), name='show-book'),

    path('bookings/<int:booking_id>/cancel/', BookingCancelAPIView.as_view(), name='booking-cancel'),
    path('my-bookings/', MyBookingsListView.as_view(), name='my-bookings'),
]
