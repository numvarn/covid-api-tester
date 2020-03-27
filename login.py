import requests
from pprint import pprint
import os

base = 'https://ssk-covid19.herokuapp.com'
endpoint = 'api/login'

url = os.path.join(base, endpoint)

myobj = {
    'username': 'admin',
    'password': 'sskrucovid2019'
}

response = requests.post(url, data=myobj)
data = response.json()

pprint(data)