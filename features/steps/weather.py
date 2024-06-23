from behave import given, when, then
from weather_requests import WeatherAPI  # Imports the WeatherAPI class

# Given step to initialize the WeatherAPI class and store it in the context
@given('the Open Weather API is available')
def step_impl(context):
    context.weather_api = WeatherAPI()  # Initializing the WeatherAPI class and store it in the context

# Step to request current weather by latitude and longitude
@when('I request the current weather by latitude "{lat}" and longitude "{lon}"')
def step_impl(context, lat, lon):
    context.response = context.weather_api.get_weather_by_lat_lon(lat, lon)  # Make the API call
    context.response_text = context.response.text  # Store response text in the context
    context.response_json = context.response.json()  # Store response JSON in the context
    print(f"URL: {context.response.url}")  # Print the request URL
    print(f"Status Code: {context.response.status_code}")  # Print the response status code
    print(f"Response: {context.response_text}")  # Print the response text

# Step to request current weather by city name
@when('I request the current weather for city "{city}"')
def step_impl(context, city):
    context.response = context.weather_api.get_weather_by_city(city)  # Make the API call
    context.response_text = context.response.text  # Store response text in the context
    context.response_json = context.response.json()  # Store response JSON in the context
    print(f"URL: {context.response.url}")  # Print the request URL
    print(f"Status Code: {context.response.status_code}")  # Print the response status code
    print(f"Response: {context.response_text}")  # Print the response text

# Step to request current weather by city name with specific units
@when('I request the current weather for "{city}" with units "{units}"')
def step_impl(context, city, units):
    context.response = context.weather_api.get_weather_by_city(city, units)  # Make the API call
    context.response_text = context.response.text  # Store response text in the context
    context.response_json = context.response.json()  # Store response JSON in the context
    print(f"URL: {context.response.url}")  # Print the request URL
    print(f"Status Code: {context.response.status_code}")  # Print the response status code
    print(f"Response: {context.response_text}")  # Print the response text

# Step to request current weather with invalid parameters to test error
@when('I request the current weather with invalid parameters')
def step_impl(context):
    context.response = context.weather_api.get_weather_with_invalid_params()  # Make the API call with invalid parameters
    context.response_text = context.response.text  # Store response text in the context
    print(f"URL: {context.response.url}")  # Print the request URL
    print(f"Status Code: {context.response.status_code}")  # Print the response status code
    print(f"Response: {context.response_text}")  # Print the response text

# Step to request current weather with an invalid API key to test authentication error
@when('I request the current weather with an invalid API key')
def step_impl(context):
    context.response = context.weather_api.get_weather_with_invalid_api_key()  # Make the API call with an invalid API key
    context.response_text = context.response.text  # Store response text in the context
    print(f"URL: {context.response.url}")  # Print the request URL
    print(f"Status Code: {context.response.status_code}")  # Print the response status code
    print(f"Response: {context.response_text}")  # Print the response text

# Step to simulate a server error (HTTP 500)
@when('I request the current weather and the server is down')
def step_impl(context):
    context.response = context.weather_api.simulate_server_down()  # Simulate a server error
    context.response_text = context.response.text  # Store response text in the context
    print(f"URL: {context.response.url}")  # Print the request URL
    print(f"Status Code: {context.response.status_code}")  # Print the response status code
    print(f"Response: {context.response_text}")  # Print the response text

# Step to check that the response status code is 200 (OK)
@then('the response status code should be 200')
def step_impl(context):
    print(f"Expected: 200, Actual: {context.response.status_code}")  # Print expected and actual status codes
    assert context.response.status_code == 200, f"Expected status code 200 but got {context.response.status_code}"  # Assert the status code is 200

# Step to validate that the response contains the current weather data
@then('the response should contain the current weather data')
def step_impl(context):
    context.weather_api.validate_current_weather_data(context.response_json)  # Validate the response JSON

# Step to check that the response status code is 400 (Bad Request)
@then('the response status code should be 400')
def step_impl(context):
    print(f"Expected: 400, Actual: {context.response.status_code}")  # Print expected and actual status codes
    assert context.response.status_code == 400, f"Expected status code 400 but got {context.response.status_code}"  # Assert the status code is 400

# Step to check that the response status code is 401 (Unauthorized)
@then('the response status code should be 401')
def step_impl(context):
    print(f"Expected: 401, Actual: {context.response.status_code}")  # Print expected and actual status codes
    assert context.response.status_code == 401, f"Expected status code 401 but got {context.response.status_code}"  # Assert the status code is 401

# Step to check that the response status code is in the 500 range (Server Error)
@then('the response status code should be 5xx')
def step_impl(context):
    print(f"Expected: 5xx, Actual: {context.response.status_code}")  # Print expected and actual status codes
    assert 500 <= context.response.status_code < 600, f"Expected status code in range 5xx but got {context.response.status_code}"  # Assert the status code is in the 500 range

# Step to validate that the response contains temperature in Celsius
@then('the response should contain temperature in Celsius')
def step_impl(context):
    response_json = context.response_json  # Get the response JSON from the context
    print(f"Response JSON: {response_json}")  # Print the response JSON
    assert 'main' in response_json, "Response does not contain 'main' key"  # Assert 'main' key exists
    assert 'temp' in response_json['main'], "Response does not contain 'temp' key"  # Assert 'temp' key exists
    assert response_json['main']['temp'] is not None, "Temperature value is None"  # Assert temperature is not None

# Step to check that the response status code is 404 (Not Found)
@then('the response status code should be 404')
def step_impl(context):
    print(f"Expected: 404, Actual: {context.response.status_code}")  # Print expected and actual status codes
    assert context.response.status_code == 404, f"Expected status code 404 but got {context.response.status_code}"  # Assert the status code is 404

# Step to check that the response contains an error message
@then('the response should contain an error message')
def step_impl(context):
    response_json = context.response_json  # Get the response JSON from the context
    print(f"Response JSON: {response_json}")  # Print the response JSON
    assert 'message' in response_json, "Response does not contain 'message' key"  # Assert 'message' key exists
    assert response_json['cod'] == '404', f"Expected cod 404 but got {response_json['cod']}"  # Assert 'cod' is 404

# Step to print the full response
@then('print the response')
def step_impl(context):
    print(f"Full Response: {context.response_text}")  # Print the full response text
    assert True  # This step always passes
