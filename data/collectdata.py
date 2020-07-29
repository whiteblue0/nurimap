

import requests, pprint
import urllib.request as request
import json
import csv
from time import sleep
def getMarkerPosition(query):
    with open('key.json', 'r') as f:
        data = json.load(f)
        X_NCP_APIGW_API_KEY_ID = data['X-NCP-APIGW-API-KEY-ID']
        X_NCP_APIGW_API_KEY = data['X-NCP-APIGW-API-KEY']
    f.close()

    url = f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={query}"

    # body = request.Request(url)
    # body.add_header("X-NCP-APIGW-API-KEY-ID",X_NCP_APIGW_API_KEY_ID)
    # body.add_header("X-NCP-APIGW-API-KEY",X_NCP_APIGW_API_KEY)

    res = requests.get(url, headers={
        "X-NCP-APIGW-API-KEY-ID":X_NCP_APIGW_API_KEY_ID,
        "X-NCP-APIGW-API-KEY":X_NCP_APIGW_API_KEY
    })
    pprint.pprint(res.json())
    if res.json().get('addresses'):
        latitude = res.json().get('addresses')[0].get('x')
        longtitude = res.json().get('addresses')[0].get('y')
        # sleep(2)
        print(latitude,longtitude)

        return latitude, longtitude
    else:
        return False, False

def getMarkerPositionByKakao(query):
    with open('key.json', 'r') as f:
        data = json.load(f)
        KAKAO_REST_API_KEY = data['KAKAO-REST-API-KEY']
    f.close()

    url = f"https://dapi.kakao.com/v2/local/search/address.json?query={query}"


    res = requests.get(url, headers={
        "Authorization": f"KakaoAK {KAKAO_REST_API_KEY}",
    })

    pprint.pprint(res.json())
    if res.json().get('documents'):
        latitude = res.json().get('documents')[0].get('x')
        longtitude = res.json().get('documents')[0].get('y')
        # sleep(2)
        print(latitude,longtitude)

        return latitude, longtitude
    else:
        
        return False, False

def getUnknownPosition():
    with open('unknown.csv' ,'r', encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            count += 1
            latitude, longtitude = getMarkerPositionByKakao(row[2])
            if latitude and longtitude:
                with open("kakako.csv", 'a', encoding="utf-8", newline="") as a:
                    print(row)
                    print(latitude,longtitude)
                    writer = csv.writer(a)
                    writer.writerow([row[0],row[1],latitude,longtitude])
            else:
                with open("not_found.csv", 'a', encoding="utf-8", newline="") as na:
                    print("좌표를 찾을수 없습니다:",row)
                    nwriter = csv.writer(na)
                    nwriter.writerow([row[0],row[1],row[2]])

        

        

# getMarkerPosition("경북 포항시 북구 흥해로")
# getMarkerPositionByKakao("전라남도 무안군 해제면 현해로")

getUnknownPosition()
