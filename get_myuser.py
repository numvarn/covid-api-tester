import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
import os

url = 'http://127.0.0.1:8000'
endpoint = 'get/myuser'
token = "Token "

response = requests.get(os.path.join(url, endpoint), headers={'Authorization': token})
data = response.json()

pprint(data)

user_id = data['results'][0]['id']
print("User id : {}".format(user_id))
