import requests
from pprint import pprint
import os
import json

# base = 'http://127.0.0.1:8000'

base = 'https://ssk-covid19.herokuapp.com'
endpoint = 'post/assessment'

url = os.path.join(base, endpoint)

myobj = {
    "account" : '1',
    "age" : '40',
    "home_subdistrict" : "หนองครก",
    "home_district" : "อำเภอเมืองศรีสะเกษ",
    "home_province" : "ศรีสะเกษ",

    "q1": "no",
    "q1_country": "",
    "q1_date": "",

    "q2": "yes",
    "q2_occupation": "สถานบันเทิง",
    "q2_occupation_etc": "",

    "q3": "no",
    "q3_relation": "",
    "q3_relation_detail": "",
    "q3_patient_type": '0',

    "q4": "no",

    "q5": "yes",
    "q5_risk_area": "วัดหว้าเอน ต.โพรงมะเดื่อ 15 มีนาคม 2563",
    "q5_risk_etc": "",
    "q5_risk_date": "",

    "q6_symptom": "มีไข้,ไอ,จาม,หายใจลำบาก หอบเหนื่อย",

    "q7": "no",
    "q7_place": "",
    "q7_place_des": "",
}

response = requests.post(url, data=myobj)
data = response.json()
pprint(data)

