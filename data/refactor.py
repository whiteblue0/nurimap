import csv
import time

def refineStr(col):
    if "(" in col:
        braceS = col.find("(")
        braceE = col.find(")")
        print(braceS,braceE)
        if braceS == 0:
            result = col[braceE+1:]
        elif braceE == (len(col)-1):
            result = col[:braceS]
        else:
            result = col[:braceS] + col[braceE+1:]
        return result
    else:
        return col
        


with open('data.csv', 'r', encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        name = refineStr(row[0])
        market = refineStr(row[1])
        address = refineStr(row[2])
        print('name:',name)
        print('market:',market)
        print('address:',address,end="\n\n")
        time.sleep(1.5)

# col = "테스트(테스트다)"
# if "(" in col:
#     s = col.find("(")
#     e = col.find(")")
#     result = col[:s] + col[e+1:]
#     print(s,e)
#     print(col[99:])
#     print(result)