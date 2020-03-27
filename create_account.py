import requests
from pprint import pprint
import os

base = 'https://ssk-covid19.herokuapp.com'
endpoint = 'api/regis'

url = os.path.join(base, endpoint)

myobj = {
    'username' : 'kewarin.p@sskru.ac.th',
    'password' : 'numvarn',
    'email' : 'kewarin.p@sskru.ac.th',
    'first_name' : 'เกวรินทร์',
    'last_name' : 'ประมวล',
}

response = requests.post(url, data=myobj)
data = response.json()

pprint(data)