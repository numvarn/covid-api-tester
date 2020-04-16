import requests
from pprint import pprint
import os

token = 'Token '

base = 'http://127.0.0.1:8000'
endpoint = 'api/checkedin'

url = os.path.join(base, endpoint)

myobj = {
    'account' : 1,
    'latitude' : 15.246758,
    'longitude' : 104.870461,
    'status' : 1,
}

response = requests.post(url, data=myobj, headers={'Authorization': token})

print("Checked-in \n")
data = response.json()
pprint(data)
print("\n")

