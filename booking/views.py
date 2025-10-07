from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Movie, Show, Booking
from .serializers import (
    UserSerializer, MovieSerializer, ShowSerializer,
    BookingSerializer
)

# -------------------
# User signup
# -------------------
class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


# -------------------
# List all movies
# -------------------
class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]


# -------------------
# List shows for a specific movie
# -------------------
class MovieShowsListView(generics.ListAPIView):
    serializer_class = ShowSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        return Show.objects.filter(movie_id=movie_id)


# -------------------
# Book a seat for a show
# -------------------
class ShowBookAPIView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, show_id, *args, **kwargs):
        user = request.user
        show = get_object_or_404(Show, id=show_id)
        seat_number = request.data.get('seat_number')

        # Check if seat is already booked
        if Booking.objects.filter(show=show, seat_number=seat_number, status='booked').exists():
            return Response({"error": "Seat already booked"}, status=status.HTTP_400_BAD_REQUEST)

        booking = Booking.objects.create(
            user=user,
            show=show,
            seat_number=seat_number,
            status='booked'
        )
        return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)


# -------------------
# Cancel a booking
# -------------------
class BookingCancelAPIView(generics.UpdateAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, booking_id, *args, **kwargs):
        booking = get_object_or_404(Booking, id=booking_id, user=request.user)
        booking.status = 'cancelled'
        booking.save()
        return Response(BookingSerializer(booking).data)


# -------------------
# List user's bookings
# -------------------
class MyBookingsListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
