#Here we have our test scenarios
Feature: Open Weather API Testing

  Scenario: Get current weather data by latitude and longitude
    Given the Open Weather API is available
    When I request the current weather by latitude "35.6895" and longitude "139.6917"
    Then the response status code should be 200
    And the response should contain the current weather data
    And print the response

  Scenario: Get current weather data by city name
    Given the Open Weather API is available
    When I request the current weather for city "London"
    Then the response status code should be 200
    And the response should contain the current weather data
    And print the response

  Scenario: Get current weather data with different units of measurement
    Given the Open Weather API is available
    When I request the current weather for "London" with units "metric"
    Then the response status code should be 200
    And the response should contain temperature in Celsius
    And print the response

  Scenario: Get current weather data with invalid parameters
    Given the Open Weather API is available
    When I request the current weather with invalid parameters
    Then the response status code should be 400
    And print the response

  Scenario: Get current weather data with invalid API key
    Given the Open Weather API is available
    When I request the current weather with an invalid API key
    Then the response status code should be 401
    And print the response

  Scenario: Simulate server error
    Given the Open Weather API is available
    When I request the current weather and the server is down
    Then the response status code should be 5xx
    And print the response

  Scenario: Get current weather data with invalid city name
    Given the Open Weather API is available
    When I request the current weather for city "InvalidCity"
    Then the response status code should be 404
    And the response should contain an error message
    And print the response
