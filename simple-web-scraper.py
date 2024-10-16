import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.prettify()

url = "http://example.com"  # Put the URL you want to scrape here
print(scrape_website(url))