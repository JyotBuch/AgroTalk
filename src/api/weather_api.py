import requests
from datetime import datetime

import sys
sys.path.append("/Users/jyotbuch/AgroTalk/src")

from utils.config import ACCUWEATHER_API_KEY

class AccuWeatherAPI:
    """
    A class to fetch weather data from AccuWeather for agriculture purposes.
    It returns current weather conditions and a 7-day forecast.
    """

    def __init__(self, lat, lon, metric=True):
        """
        Initialize with latitude, longitude, and unit preference.
        :param lat: Latitude of the location.
        :param lon: Longitude of the location.
        :param metric: Use metric units (True) or imperial (False).
        """
        self.api_key = ACCUWEATHER_API_KEY
        self.lat = lat
        self.lon = lon
        self.metric = metric
        self.location_key = self.get_location_key()

        if not self.location_key:
            raise ValueError("Invalid location key. Check API response.")
    
    def get_location_key(self):
        """
        Retrieve the AccuWeather location key using latitude and longitude.
        """
        url = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search"
        params = {"apikey": self.api_key, "q": f"{self.lat},{self.lon}"}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("Key")
    
    def get_current_weather(self):
        """
        Fetch the current weather conditions.
        """
        url = f"http://dataservice.accuweather.com/currentconditions/v1/{self.location_key}"
        params = {"apikey": self.api_key, "details": "true"}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if not data:
            return {}
        
        current = data[0]
        return {
            "temperature": current["Temperature"]["Metric"]["Value"] if self.metric else current["Temperature"]["Imperial"]["Value"],
            "humidity": current.get("RelativeHumidity"),
            "pressure": current["Pressure"]["Metric"]["Value"] if self.metric else current["Pressure"]["Imperial"]["Value"],
            "wind_speed": current["Wind"]["Speed"]["Metric"]["Value"] if self.metric else current["Wind"]["Speed"]["Imperial"]["Value"],
            "uv_index": current.get("UVIndex"),
            "weather_text": current.get("WeatherText")
        }
    
    def get_five_day_forecast(self):
        """
        Fetch the 5-day weather forecast.
        """
        url = f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{self.location_key}"
        params = {"apikey": self.api_key, "details": "true", "metric": str(self.metric).lower()}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        forecast = []
        for day in data.get("DailyForecasts", []):
            forecast.append({
                "date": datetime.utcfromtimestamp(day["EpochDate"]).strftime("%Y-%m-%d"),
                "min_temp": day["Temperature"]["Minimum"]["Value"],
                "max_temp": day["Temperature"]["Maximum"]["Value"],
                "humidity": day["Day"].get("RelativeHumidity"),
                "uv_index": day["Day"].get("UVIndex"),
                "rain_probability": day["Day"].get("PrecipitationProbability")
            })
        return forecast
    
    def get_weather_summary(self):
        """
        Return current weather and 5-day forecast.
        """
        current_weather = self.get_current_weather()
        forecast = self.get_five_day_forecast()
        
        return {
            "current_weather": current_weather,
            "forecast": forecast
        }

# # Example usage
# if __name__ == "__main__":
#     lat, lon = 40.51, -88.40  # Example coordinates
#     weather_api = AccuWeatherAPI(lat=lat, lon=lon, metric=True)
    
#     weather_summary = weather_api.get_weather_summary()
    
#     print("Current Weather:")
#     for key, value in weather_summary["current_weather"].items():
#         print(f"  {key}: {value}")
    
#     print("\n5-Day Forecast:")
#     for day in weather_summary["forecast"]:
#         print(day)
