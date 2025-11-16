"""
Models for the listings app in the ALX Travel application.  
"""

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Listing(models.Model):
    """
    Represents a property that can be booked on the travel platform.
    """

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    price_per_night = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    max_guests = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.title} ({self.location})"


class Booking(models.Model):
    """
    Represents a booking made by a guest for a specific listing.
    """

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
    ]

    listing = models.ForeignKey(
        Listing,
        related_name="bookings",
        on_delete=models.CASCADE,
    )
    guest_name = models.CharField(max_length=255)
    guest_email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()
    num_guests = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="pending",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Booking #{self.id} for {self.listing.title} ({self.status})"


class Review(models.Model):
    """
    Represents a review left by a guest for a listing
    (optionally tied to a specific booking).
    """

    listing = models.ForeignKey(
        Listing,
        related_name="reviews",
        on_delete=models.CASCADE,
    )
    booking = models.ForeignKey(
        Booking,
        related_name="reviews",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Optional link to a specific booking",
    )
    reviewer_name = models.CharField(max_length=255)
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
        help_text="Rating from 1 (worst) to 5 (best)",
    )
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"Review {self.rating}/5 for {self.listing.title}"
