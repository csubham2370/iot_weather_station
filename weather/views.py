from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import WeatherReading
from .serializers import WeatherReadingSerializer
from django.shortcuts import render
import requests


def dashboard(request):
    return render(request,"weather/dashboard.html")

@api_view(["POST"])
def create_weather_reading(request):

    serializer = WeatherReadingSerializer(data=request.data)
   
    if serializer.is_valid():
        # print(serializer.data)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# GET - Get latest weather reading
@api_view(["GET"])
def latest_weather_reading(request):

    reading = WeatherReading.objects.order_by( "-created_at").first()

    if reading is None:
        return Response(
            {
                "message": "No weather data available"
            },
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = WeatherReadingSerializer(reading)

    return Response(serializer.data,status=status.HTTP_200_OK)



@api_view(["GET"])
def current_location_name(request):

    latitude = request.GET.get("lat")
    longitude = request.GET.get("lon")

    if not latitude or not longitude:
        return Response(
            {
                "error": "Latitude and longitude are required"
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    try:

        response = requests.get(
            "https://nominatim.openstreetmap.org/reverse",
            params={
                "lat": latitude,
                "lon": longitude,
                "format": "jsonv2",
                "addressdetails": 1,
            },
            headers={
                "User-Agent": "iot-weather-station-learning-project/1.0"
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        address = data.get(
            "address",
            {}
        )

        city = (
            address.get("city")
            or address.get("town")
            or address.get("village")
            or address.get("municipality")
            or address.get("county")
        )

        state_name = address.get(
            "state"
        )

        country = address.get(
            "country"
        )

        location_parts = [
            city,
            state_name,
            country,
        ]

        location_parts = [
            part
            for part in location_parts
            if part
        ]

        # location_name = ", ".join(
        #     location_parts
        # )

        return Response({
            # "location_name": location_name,
            "latitude": latitude,
            "longitude": longitude,
        })


    except requests.RequestException:

        return Response(
            {
                "error": "Unable to find location name"
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )