# web_scraper/scraper.py
import requests
from bs4 import BeautifulSoup

def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Example: Extract all image sources
    images = soup.find_all('img')
    image_urls = [img['src'] for img in images if img.get('src')]
    return image_urls
