import requests
from pprint import pprint
import os
import json

token = 'Token '

base = 'http://127.0.0.1:8000'
endpoint = 'post/self-screen'

url = os.path.join(base, endpoint)

myobj = {
    "account" : 1,
    "assessment_score": 1,
    "assessment_suggest": "ให้เฝ้าระวังอาการตนเอง ถ้ามีอาการไข้ ร่วมกับ อาการระบบทางเดินหายใจ (มีทั้ง 2 อาการ) ให้ติดต่อสถานพยาบาลทันที",
}

js = json.loads(json.dumps(myobj))
# print(js)

response = requests.post(url, data=myobj, headers={'Authorization': token})

data = response.json()
pprint(data)

