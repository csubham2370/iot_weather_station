from rest_framework import serializers

from .models import WeatherReading


class WeatherReadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherReading

        fields = [
            "id",
            "device_id",
            # "location_name",
            # "latitude",
            # "longitude",
            "temperature",
            "humidity",
            # "pressure",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]