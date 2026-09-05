from django.db import models


class WeatherReading(models.Model):

    device_id = models.CharField(max_length=50)

    # location_name = models.CharField(max_length=100,blank=True)

    # latitude = models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)

    # longitude = models.DecimalField(max_digits=9,decimal_places=6,null=True,blank=True)

    temperature = models.FloatField()

    humidity = models.FloatField()

    # pressure = models.FloatField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device_id} - {self.temperature}°C"