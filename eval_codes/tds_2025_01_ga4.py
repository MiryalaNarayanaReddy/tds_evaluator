import re 
from bs4 import BeautifulSoup
import requests
import json

def q_scrape_imdb_movies(question):
     
    min_rating, max_rating = 6,8
    match = re.search(r'rating between (\d+) and (\d+)', question)
    if match:
        # int(match.group(1)), int(match.group(2))
        min_rating = int(match.group(1))
        max_rating = int(match.group(2))

    url = f"https://www.imdb.com/search/title/?user_rating={min_rating},{max_rating}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movies = []
    for item in soup.select(".ipc-metadata-list-summary-item")[:25]:
        id_tag = item.select_one(".ipc-lockup-overlay")
        title_tag = item.select_one(".ipc-title")
        year_tag = item.select_one(".dli-title-metadata-item")
        rating_tag = item.select_one(".ipc-rating-star--rating")
        
        id_match = id_tag["href"].split("/title/")[1].split("/")[0] if id_tag and "href" in id_tag.attrs else None
        
        movies.append({
            "id": id_match,
            "title": title_tag.text if title_tag else None,
            "year": year_tag.text if year_tag else None,
            "rating": rating_tag.text if rating_tag else None
        })
    
    return movies



def q_bbc_weather_api(question):
    # Use regex to extract the city name.
    # This regex looks for 'weather forecast for' followed by a city name (letters and spaces)
    match = re.search(r"weather forecast for\s+([A-Za-z\s]+)", question, re.IGNORECASE)
    if not match:
        return json.dumps({"error": "City not found in the input text."})
    
    city = match.group(1).strip()
    
    # Retrieve the location ID using the BBC locator service.
    locator_params = {
        "api_key": "AGbFAKx58hyjQScCXIYrxuEwJh2W2cmv",
        "stack": "aws",
        "locale": "en",
        "filter": "international",
        "place-types": "settlement,airport,district",
        "order": "importance",
        "s": city,
        "a": "true",
        "format": "json"
    }
    locator_url = "https://locator-service.api.bbci.co.uk/locations"
    locator_response = requests.get(locator_url, params=locator_params, verify=False)
    locator_data = locator_response.json()
    
    # Extract the first matching location's ID.
    try:
        location_id = locator_data["response"]["results"]["results"][0]["id"]
    except (KeyError, IndexError):
        return json.dumps({"error": f"Location ID for city '{city}' could not be found."})
    
    # Fetch the weather forecast for the given location.
    forecast_url = f"https://weather-broker-cdn.api.bbci.co.uk/en/forecast/aggregated/{location_id}"
    forecast_response = requests.get(forecast_url, verify=False)
    forecast_data = forecast_response.json()
    
    # Build a dictionary mapping each date to its enhanced weather description.
    forecast = {
        entry["summary"]["report"]["localDate"]: entry["summary"]["report"]["enhancedWeatherDescription"]
        for entry in forecast_data.get("forecasts", [])
    }
    
    # Return the result as a JSON-formatted string.
    return forecast