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
