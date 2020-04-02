import requests
from pprint import pprint
import os

token = 'Token 62b62f18f5a7024c4a94035a7bc32ba3704d80dd'

# base = 'http://127.0.0.1:8000'
base = 'https://ssk-covid19.herokuapp.com'
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

