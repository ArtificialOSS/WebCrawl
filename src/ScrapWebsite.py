import requests
import re

from bs4 import BeautifulSoup

def ScrapWebsite(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    text = re.sub(r'\n{2,}', '\n', text)
    return text