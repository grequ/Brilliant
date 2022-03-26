import requests
import pandas as pd

filedirector = 'C:/Users/GrzegorzChuchra/Google Drive/machine learning/2. Praca z danymi w języku Python - Numpy i Pandas/'

url='https://api.nfz.gov.pl/app-stat-api-ra/monthly-provisions?page=1&limit=24&format=json'
response=requests.get(url)


refundacja=pd.DataFrame(response.json()['data'])
listalekow=['Aclasta','Adakveo','Afinitor','Clexane']


import time
df=pd.DataFrame(columns=['medicine-product','international-name','code','dose','pack','quantity','refund','donation','contribution-of-patient','value'])
for lek in listalekow:
    print(lek)
    try:
        url='https://api.nfz.gov.pl/app-stat-api-ra/provisions?format=json&medicineProduct='+lek.lower()
        response=requests.get(url)
        for i in range(len(response.json()['data']['data'])):
            df=df.append(pd.DataFrame(response.json()['data']['data'][i]['attributes'],index=[0]))
    except:
        continue
    time.sleep(1)

df.to_excel(filedirector + 'refundacjaapteczna1.xlsx')