"""
    Serializers for the listings app in the ALX Travel application.
"""

from rest_framework import serializers

from .models import Listing, Booking, Review


class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Listing model.
    This converts Listing instances <-> JSON.
    """

    class Meta:
        model = Listing
        # You can use "__all__" or a specific list of fields
        fields = "__all__"
        # OR, if you want to be explicit:
        # fields = [
        #     "id",
        #     "title",
        #     "description",
        #     "location",
        #     "price_per_night",
        #     "max_guests",
        #     "created_at",
        #     "updated_at",
        # ]


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.
    """

    # Optional nice touch: show the listing title read-only in responses
    listing_title = serializers.CharField(source="listing.title", read_only=True)

    class Meta:
        model = Booking
        fields = "__all__"
        # Or explicitly, e.g.:
        # fields = [
        #     "id",
        #     "listing",
        #     "listing_title",  # extra read-only helper field
        #     "check_in",
        #     "check_out",
        #     "num_guests",
        #     "created_at",
        # ]


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model.
    """

    # Optional: include listing title in the output
    listing_title = serializers.CharField(source="listing.title", read_only=True)

    class Meta:
        model = Review
        fields = "__all__"
        # If you want to be explicit, you can replace "__all__" with:
        # fields = [
        #     "id",
        #     "listing",
        #     "listing_title",
        #     "rating",
        #     "comment",
        #     "created_at",
        # ]