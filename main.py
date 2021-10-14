import sys
import requests


response = requests.get('https://cbr.ru/scripts/xml_daily.asp')
print(response.text)