'''
REST API Tester

Author : Phisan Sookkhee
Date : 27 March 2020, 11:57
Base url : https://ssk-covid19.herokuapp.com

step 1. Log-in with user, password
step 2. Get current user with token
stop 2. Check-in with current user id
'''
import requests
from pprint import pprint
import os

Token = None
User_ID = None

base = 'https://ssk-covid19.herokuapp.com'

'''
Step 1. Log-in and get Token
'''
endpoint_login = 'api/login'

url = os.path.join(base, endpoint_login)

myobj = {
    'username': 'admin',
    'password': 'sskrucovid2019'
}

response = requests.post(url, data=myobj)
data = response.json()

if data.get('token'):
    Token = "Token "+data['token']
    print("Log in Successed, Your token is : {}".format(Token))

else:
    print("Invalid Username or Password !!")

# ---------------------------------------------------
'''
Step 2. Get current user-profile

if log-in success you will token from system
'''
endpoint_get_myuser = 'get/myuser'

url = os.path.join(base, endpoint_get_myuser)

response = requests.get(url, headers={'Authorization': Token})
data = response.json()

print("Current User Data")
pprint(data)

User_ID = data['results'][0]['id']

# ---------------------------------------------------

'''
Step 3. Check-in

if log-in success you will token from system
'''

endpoint_check_in = 'api/checkedin'
url = os.path.join(base, endpoint_check_in)

myobj = {
    'account' : User_ID,
    'latitude' : 15.143479, 
    'longitude' : 104.256276, 
    'status' : 1,
}

response = requests.post(url, data=myobj, headers={'Authorization': Token})

print("Checked-in")
pprint(myobj)
# ---------------------------------------------------