from django.test import TestCase

# Create your tests here.
import requests
from bs4 import BeautifulSoup

r = requests.get('https://github.com/trending/python')
soup = BeautifulSoup(r.content, 'html.parser')

print(soup)