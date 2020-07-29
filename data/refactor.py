import csv
import time
from collectdata import getMarkerPosition

def refineStr(col):
    stack = []
    for string in col:
        if string == "\"":
            col = col.replace("\"","")
    
    if "(" in col:
        braceS = col.find("(")
        braceE = col.find(")")
        print("BRACE DETECTED:",braceS,braceE)
        if braceS == 0:
            result = col[braceE+1:]
        elif braceE == (len(col)-1):
            result = col[:braceS]
        else:
            result = col[:braceS] + col[braceE+1:]
        return result
    else:
        return col
def cutAddressDetail(col):
    lst = col.split(' ')
with open('data.csv', 'r', encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    with open('refined_data.csv', "a", encoding="utf-8", newline="") as w:
        writer = csv.writer(w)
        count = 0
        for row in reader:
            count += 1
            print(row)
            # 25429부터 시작
            if count < 25429:
                continue
            name = refineStr(row[0])
            market = refineStr(row[1])
            address = refineStr(row[2])
            if len(address.split(" ")) > 4:
                address = address.split(" ")
                address = address[:4]
                address = " ".join(address)
            if (address == "소재지") or (address == "없음"):
                continue
            lati,longti = getMarkerPosition(address)
            if lati== False and longti == False:
                with open('unknown.csv','a', encoding="utf-8", newline="") as nw:
                    nwriter = csv.writer(nw)
                    nwriter.writerow([name,market,address])
                    print(f"이 주소를 찾을 수 없습니다. 주소: {address}")
                    nw.close()

                continue
            print('name:',name)
            print('market:',market)
            print('address:',address)
            print('X,Y:',lati,longti,end="\n\n")
            writer.writerow([name,market,lati,longti])
            # time.sleep(1.5)