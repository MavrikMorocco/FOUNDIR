# web_scraper/views.py
from django.shortcuts import render
from .scraper import fetch_url, parse_html

def display_images(request, url):
    html_content = fetch_url(url)
    images = parse_html(html_content) if html_content else []
    return render(request, 'web_scraper/display_images.html', {'images': images})
