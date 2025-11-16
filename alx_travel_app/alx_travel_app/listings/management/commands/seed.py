from django.core.management.base import BaseCommand
from django.utils import timezone

from ...models import Listing, Booking, Review 


class Command(BaseCommand):
    help = "Seed the database with sample listings (and optionally bookings/reviews)."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Starting database seeding..."))

        # ---- Basic safety: avoid duplicating data every time ----
        if Listing.objects.exists():
            self.stdout.write(
                self.style.WARNING(
                    "Listings already exist. Skipping seeding to avoid duplicates."
                )
            )
            return

        # ---- Sample listings data ----
        listings_data = [
            {
                "title": "Beachfront Apartment",
                "description": "Lovely sea-facing apartment with 2 bedrooms and fast Wi-Fi.",
                "location": "Cape Town, South Africa",
                "price_per_night": 1500.00,
                "max_guests": 4,
            },
            {
                "title": "Mountain View Cabin",
                "description": "Rustic cabin with a fireplace and hiking trails nearby.",
                "location": "Drakensberg, South Africa",
                "price_per_night": 900.00,
                "max_guests": 2,
            },
            {
                "title": "City Center Studio",
                "description": "Modern studio close to public transport and restaurants.",
                "location": "Johannesburg, South Africa",
                "price_per_night": 700.00,
                "max_guests": 2,
            },
            {
                "title": "Luxury Safari Lodge",
                "description": "All-inclusive safari lodge experience with game drives.",
                "location": "Kruger National Park, South Africa",
                "price_per_night": 3000.00,
                "max_guests": 6,
            },
        ]

        created_listings = []

        # ---- Create listings ----
        for data in listings_data:
            listing = Listing.objects.create(**data)
            created_listings.append(listing)
            self.stdout.write(
                self.style.SUCCESS(f"Created listing: {listing.title}")
            )

        from datetime import timedelta
        now = timezone.now().date()
        
        for listing in created_listings:
            # Example booking
            booking = Booking.objects.create(
                listing=listing,
                check_in=now,
                check_out=now + timedelta(days=3),
                num_guests=min(2, listing.max_guests),
            )
            self.stdout.write(
                self.style.SUCCESS(f"Created booking for listing: {listing.title}")
            )
        
            # Example review
            Review.objects.create(
                listing=listing,
                rating=5,
                comment=f"Amazing stay at {listing.title}!",
            )
            self.stdout.write(
                self.style.SUCCESS(f"Created review for listing: {listing.title}")
            )

        self.stdout.write(self.style.SUCCESS("Seeding completed successfully."))
