# Weather API Test Automation

This repository contains automated tests for the Open Weather API using the Behave framework. The tests cover various scenarios like: requesting weather data by city, latitude and longitude, handling invalid parameters, and simulating server errors.

## Prerequisites

- Python 3.7+
- pip (Python package installer)


## Setup Instructions

### Clone the Repository

```bash
git clone git@github.com:vanessaalvesqa/openweather.git
cd to your folder where you clone the repo

pip install behave
pip install behave-html-formatter

## Running
behave

## Running with reports
behave -f behave_html_formatter:HTMLFormatter -o reports/report.html

## Opening the reports
start reports/report.html
