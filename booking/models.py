from django.db import models
from django.conf import settings
from django.db.models import Q, UniqueConstraint, Index

class Movie(models.Model):
    title = models.CharField(max_length=255)
    duration_minutes = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} ({self.duration_minutes}m)"


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='shows')
    screen_name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    total_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.movie.title} @ {self.screen_name} on {self.date_time}"


class Booking(models.Model):
    STATUS_BOOKED = 'booked'
    STATUS_CANCELLED = 'cancelled'
    STATUS_CHOICES = [
        (STATUS_BOOKED, 'Booked'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='bookings')
    seat_number = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_BOOKED)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.show} - seat {self.seat_number} [{self.status}]"

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["show", "seat_number"],
                condition=Q(status='booked'),  # Use string literal or STATUS_BOOKED
                name="unique_booked_seat_per_show"
            )
        ]
        indexes = [
            Index(fields=['show', 'seat_number']),
            Index(fields=['show', 'status']),
        ]
