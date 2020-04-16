import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
import os


url = 'http://127.0.0.1:8000'
endpoint = 'get/mycheckedin'
token = 'Token '

response = requests.get(os.path.join(url, endpoint), headers={'Authorization': token})
data = response.json()

pprint(data)
