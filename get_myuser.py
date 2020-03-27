import requests
from requests.auth import HTTPBasicAuth
from pprint import pprint
import os

url = 'https://ssk-covid19.herokuapp.com'
endpoint = 'get/myuser'
token = 'Token d035525fda947a91ac9017aa15e4f4664528ea02'

response = requests.get(os.path.join(url, endpoint), headers={'Authorization': token})
data = response.json()

pprint(data)

user_id = data['results'][0]['id']
print("User id : {}".format(user_id))