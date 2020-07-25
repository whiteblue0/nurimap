

import requests, pprint
import urllib.request as request
import json

with open('key.json', 'r') as f:
    data = json.load(f)
    X_NCP_APIGW_API_KEY_ID = data['X-NCP-APIGW-API-KEY-ID']
    X_NCP_APIGW_API_KEY = data['X-NCP-APIGW-API-KEY']
f.close()

# baseUrl = "https://openapi.naver.com/v1/search/local.json"

# query = 'jeep'

# url = f"{baseurl}?query={query}&display=30"
query = "인천시 중구 인현동 1 인현지하상가"
url = f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={query}&coordinate=127.1054328,37.3595963"

body = request.Request(url)
body.add_header("X-NCP-APIGW-API-KEY-ID",X_NCP_APIGW_API_KEY_ID)
body.add_header("X-NCP-APIGW-API-KEY",X_NCP_APIGW_API_KEY)

res = requests.get(url, headers={
    "X-NCP-APIGW-API-KEY-ID":X_NCP_APIGW_API_KEY_ID,
    "X-NCP-APIGW-API-KEY":X_NCP_APIGW_API_KEY

})

latitude = res.json().get('addresses')[0].get('x')
longtitude = res.json().get('addresses')[0].get('y')

pprint.pprint(res.json().get('addresses')[0].get('x'))
pprint.pprint(res.json().get('addresses')[0].get('y'))