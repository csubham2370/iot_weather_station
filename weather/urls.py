from django.urls import path
from . import views

urlpatterns = [

    # Dashboard
    path("",views.dashboard,name="dashboard"),

    #POST
    path("api/weather/",views.create_weather_reading,name="create_weather_reading"),

    # GET
    path("api/weather/latest/",views.latest_weather_reading,name="latest_weather_reading"),

    path("api/location/",views.current_location_name,name="current_location_name"
),
]