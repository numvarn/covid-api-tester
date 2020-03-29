import requests
from pprint import pprint
import os

token = 'Token d035525fda947a91ac9017aa15e4f4664528ea02'

# base = 'http://127.0.0.1:8000'
base = 'https://ssk-covid19.herokuapp.com'
endpoint = 'post/profile'

url = os.path.join(base, endpoint)

myobj = {
    'account': 4,
    'gender': 'หญิง',
    'age': 38,
    'nationality': 'ไทย',
    'occupation': 'อาจารย์',
    'office_address': '319 ถ.ไทพานทา',
    'office_subdistrict': 'โพธิ์',
    'office_district': 'เมือง',
    'office_province': 'ศรีสะเกษ',
    'office_phone': '0453982456',
    'home_address': '40/6',
    'home_subdistrict': 'หนองครก',
    'home_district': 'เมือง',
    'home_province': 'ศรีสะเกษ',
    'mobile_phone': '0889152456',
}


response = requests.post(url, data=myobj, headers={'Authorization': token})
data = response.json()
pprint(data)

