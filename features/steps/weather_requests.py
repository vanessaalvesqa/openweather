import requests  # Importing the requests library to make the HTTP requests

class WeatherAPI:
    # Initializing the WeatherAPI class with the base URL and API key (generated on the Open Weather site)
    def __init__(self):
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"  # Base URL for the OpenWeather API
        self.api_key = 'baa9ddc656bb87b141241ca74355c2a8'  # API key for authentication

    # Method to get weather by latitude and longitude
    def get_weather_by_lat_lon(self, lat, lon):
        params = {'lat': lat, 'lon': lon, 'appid': self.api_key}  # Parameters for the API request
        return requests.get(self.base_url, params=params)  # Makes the GET request and returns the response

    # Method to get weather by city name, with optional units
    def get_weather_by_city(self, city, units=None):
        params = {'q': city, 'appid': self.api_key}  # Parameters for the API request
        if units:  # If units are provided
            params['units'] = units  # Add units to the parameters
        return requests.get(self.base_url, params=params)  # Makes the GET request and return the response

    # Method to request weather data with invalid parameters
    def get_weather_with_invalid_params(self):
        params = {'invalid': 'invalid', 'appid': self.api_key}  # Invalid parameters
        return requests.get(self.base_url, params=params)  # Makes the GET request and returns the response

    # Method to request weather data with an invalid API key
    def get_weather_with_invalid_api_key(self, city='London'):
        params = {'q': city, 'appid': 'invalid_api_key'}  # Parameters with an invalid API key
        return requests.get(self.base_url, params=params)  # Makes the GET request and returns the response

    # Method to simulate a server error
    def simulate_server_down(self):
        return requests.get('https://httpstat.us/500')  # Makes the GET request to a URL that returns a 500 error

    # Method to validate that the response JSON contains all the required keys for weather data
    def validate_current_weather_data(self, response_json):
        required_keys = ['coord', 'weather', 'base', 'main', 'visibility', 'wind', 'clouds', 'dt', 'sys', 'timezone', 'id', 'name', 'cod']  # List of required keys
        for key in required_keys:  # Loop through each required key
            assert key in response_json, f"Key '{key}' not found in response"  # Check if the key is in the response
        # Check nested keys and array lengths in the response JSON
        assert 'lon' in response_json['coord'], "Key 'lon' not found in 'coord'"
        assert 'lat' in response_json['coord'], "Key 'lat' not found in 'coord'"
        assert len(response_json['weather']) > 0, "'weather' array is empty"
        assert 'id' in response_json['weather'][0], "Key 'id' not found in 'weather[0]'"
        assert 'main' in response_json['weather'][0], "Key 'main' not found in 'weather[0]'"
        assert 'description' in response_json['weather'][0], "Key 'description' not found in 'weather[0]'"
        assert 'icon' in response_json['weather'][0], "Key 'icon' not found in 'weather[0]'"
        assert 'temp' in response_json['main'], "Key 'temp' not found in 'main'"
        assert 'feels_like' in response_json['main'], "Key 'feels_like' not found in 'main'"
        assert 'temp_min' in response_json['main'], "Key 'temp_min' not found in 'main'"
        assert 'temp_max' in response_json['main'], "Key 'temp_max' not found in 'main'"
        assert 'pressure' in response_json['main'], "Key 'pressure' not found in 'main'"
        assert 'humidity' in response_json['main'], "Key 'humidity' not found in 'main'"
