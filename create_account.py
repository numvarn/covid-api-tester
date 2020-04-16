import requests
from pprint import pprint
import os

base = 'http://127.0.0.1:8000'
endpoint = 'api/regis'

url = os.path.join(base, endpoint)

myobj = {
    'username' : 'sirikanlaya.p@sskru.ac.th',
    'password' : 'numvarn',
    'email' : 'sirikanlaya.p@sskru.ac.th',
    'first_name' : 'สิริกัลยา',
    'last_name' : 'สุขขี',
}

response = requests.post(url, data=myobj)
data = response.json()

pprint(data)
