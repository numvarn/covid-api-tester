import requests
from pprint import pprint
import os

token = 'Token d035525fda947a91ac9017aa15e4f4664528ea02'

# base = 'http://127.0.0.1:8000'
base = 'https://ssk-covid19.herokuapp.com'
endpoint = 'api/checkedin'

url = os.path.join(base, endpoint)

myobj = {
    'account' : 6,
    'latitude' : 15.246758,
    'longitude' : 104.870461,
    'status' : 1,
}

response = requests.post(url, data=myobj, headers={'Authorization': token})

print("Checked-in \n")
data = response.json()
pprint(data)
print("\n")

