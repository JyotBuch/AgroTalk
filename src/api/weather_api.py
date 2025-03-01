import requests
from datetime import datetime
from src.config import ACCUWEATHER_API_KEY

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

    def get_location_key(self):
        """
        Retrieve the AccuWeather location key using geoposition search.
        """
        url = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search"
        params = {
            "apikey": self.api_key,
            "q": f"{self.lat},{self.lon}"
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("Key")

    def get_current_weather(self):
        """
        Fetch the current weather conditions.
        """
        url = f"http://dataservice.accuweather.com/currentconditions/v1/{self.location_key}"
        params = {
            "apikey": self.api_key,
            "details": "true"
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if not data:
            return {}
        current = data[0]
        weather_stats = {
            "temperature": current.get("Temperature", {}).get("Metric", {}).get("Value") if self.metric else current.get("Temperature", {}).get("Imperial", {}).get("Value"),
            "weather_text": current.get("WeatherText"),
            "humidity": current.get("RelativeHumidity"),
            "pressure": current.get("Pressure", {}).get("Metric", {}).get("Value") if self.metric else current.get("Pressure", {}).get("Imperial", {}).get("Value"),
            "wind_speed": current.get("Wind", {}).get("Speed", {}).get("Metric", {}).get("Value") if self.metric else current.get("Wind", {}).get("Speed", {}).get("Imperial", {}).get("Value"),
            "uv_index": current.get("UVIndex"),
            "uv_text": current.get("UVIndexText")
        }
        return weather_stats

    def get_seven_day_forecast(self):
        """
        Fetch the 5-day forecast.
        Converts epoch dates to 'YYYY-MM-DD' format.
        """
        # Using the 10-day forecast endpoint; we limit the result to 7 days.
        url = f"http://dataservice.accuweather.com/forecasts/v1/daily/10day/{self.location_key}"
        params = {
            "apikey": self.api_key,
            "details": "true",
            "metric": str(self.metric).lower()  # "true" or "false"
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        daily_forecasts = data.get("DailyForecasts", [])  # Get next 5 days

        forecast = []
        for day in daily_forecasts:
            forecast.append({
                "date": datetime.fromtimestamp(day.get("EpochDate")).strftime("%Y-%m-%d"),
                "min_temp": day.get("Temperature", {}).get("Minimum", {}).get("Value"),
                "max_temp": day.get("Temperature", {}).get("Maximum", {}).get("Value"),
                "day_description": day.get("Day", {}).get("IconPhrase"),
                "night_description": day.get("Night", {}).get("IconPhrase"),
                "humidity": day.get("Day", {}).get("RelativeHumidity"),
                "uv_index": day.get("Day", {}).get("UVIndex"),
                "rain_probability": day.get("Day", {}).get("PrecipitationProbability")
            })
        return forecast

    def get_agriculture_weather_stats(self):
        """
        Return both current weather stats and a 7-day forecast.
        """
        return {
            "current": self.get_current_weather(),
            "forecast": self.get_seven_day_forecast()
        }

# Test the class functionality
if __name__ == "__main__":
    # Example coordinates (e.g., Champaign, IL)
    lat, lon = 40.51, 88.40
    weather_api = AccuWeatherAPI(lat=lat, lon=lon, metric=True)

    stats = weather_api.get_agriculture_weather_stats()

    print("Current Weather:")
    for key, value in stats["current"].items():
        print(f"  {key}: {value}")

    print("\n5-Day Forecast:")
    for day in stats["forecast"]:
        print(day)