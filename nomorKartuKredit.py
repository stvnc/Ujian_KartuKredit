'''
    Ujian Modul 01 Job Connector Data Science Purwadhika
    Tanggal: 12 November 2019
    Soal   : 03 - Nomor Kartu Kredit
    Nama   : Vincent Angelo
'''
import json

# Adapun kriteria nomor kartu kredit yang valid adalah sebagai berikut:

# Diawali dengan angka 4, 5 atau 6.
# Terdiri atas tepat 16 digit angka.
# Hanya mengandung angka 0-9.
# Boleh dituliskan berupa grup 4 digit yang dipisahkan dengan tanda hubung "-"
# Tidak boleh terdapat 1 angka yang diulang >3x & tertulis secara beruntun, misal: 3333.
                
def checkFFS(param):
    print(param[0])
    if int(param[0]) == 4 or int(param[0]) == 5 or int(param[0]) == 6:
        return True
    else:
        return False

def checkDot(param):
    dot = '.'
    if dot in str(param):
        return False
    else:
        return True

def checkLength(param):
    if len(str(param).replace('-', '')) == 16:
        return True
    else:
        return False

def checkNumeric(param):
    if str(param).replace('-', '').isnumeric():
        return True
    else:
        return False

def checkRepetition(param):
    newList = list(str(param).replace('-', ''))
    print(newList)
    count = 0

    for i in range(len(newList)-1):
        print(count, end= "")
        if newList[i] == newList[i+1]:
            count += 1
        else: 
            count = 0
        if count >= 3:
            return False

    return True

def checkDash(param):
    dash = "-"
    if dash in str(param):
        param = param.split(dash)
        for i in param:
            if len(i) == 4:
                return True
            else:
                return False
    else:
        return True

inside = open("ccNasabah.json", "r")
out = json.load(inside)
print(out[0]['nama'])

validDict = {}
count = 0

for i in out:
    booleanList = []
    booleanList.append(checkFFS(i['noCreditCard']))
    booleanList.append(checkLength(i['noCreditCard']))
    booleanList.append(checkNumeric(i['noCreditCard']))
    booleanList.append(checkRepetition(i['noCreditCard']))
    booleanList.append(checkDash(i['noCreditCard']))
    booleanList.append(checkDot(i['noCreditCard']))
    print(booleanList)
    boolCount = 0

    for i in booleanList:
        if i == True:
            boolCount += 1
        if boolCount == 6:
            validDict[count] = 1
        else:
            validDict[count] = 0
    count += 1

print(validDict)

validData = []
invalidData = []

for i in range(len(validDict)):
    if validDict[i] == 1:
        validData.append({
            'nama': out[i]['nama'],
            'noCreditCard': out[i]['noCreditCard']
        })
    else:
        invalidData.append({
            'nama': out[i]['nama'],
            'noCreditCard': out[i]['noCreditCard']
        })

with open('ccValid.json', 'w') as outfile:
    json.dump(validData, outfile)

with open('ccInvalid.json', 'w') as outfile:
    json.dump(invalidData, outfile)
    


    


