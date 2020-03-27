import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
import os

url = 'https://ssk-covid19.herokuapp.com'
endpoint = 'get/myprofile'
token = 'Token d035525fda947a91ac9017aa15e4f4664528ea02'

response = requests.get(os.path.join(url, endpoint), headers={'Authorization': token})
data = response.json()

pprint(data)