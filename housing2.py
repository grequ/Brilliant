import pandas as pd

filedirector = 'C:/Users/GrzegorzChuchra/Google Drive/machine learning/2. Praca z danymi w języku Python - Numpy i Pandas/'
txhousing=pd.read_excel(filedirector + 'txhousing.xlsx')



txhousing['year1']='20'+txhousing['month_date'].str[4:]

txhousing.head()
txhousing['date3']=txhousing['year1']+'-'+txhousing['month_shortcut']+'-'+'01'
txhousing.to_excel(filedirector + 'txhousing_preprocessed.xlsx')

import datetime
d = datetime.datetime.strptime(txhousing['month_date'][0],'%b-%y').strftime('%d/%m/%Y')
#ta linka ponizej to jest to samo co na górze TYLKO lambda przerabia to na cała kolume a nie tak jak wyzej na jeden wiersz [0]
txhousing['month_date']=txhousing['month_date'].apply(lambda x: datetime.datetime.strptime(x,'%b-%y').strftime('%Y-%m-%d'))
txhousing['month_date']=pd.to_datetime(txhousing['month_date'])
txhousing['month_date']=txhousing['month_date'].dt.date
# txhousing['month_date']='01'+'-'+ txhousing['month_date']
txhousing['month_date']=pd.to_datetime(txhousing['month_date'])

txhousing.to_excel(filedirector + 'txhousing_preprocessed.xlsx')

# ze danych zmiennych na dane kategoryczne. Czyli ze zbioru danych np.: dochód funkacja mi dzieli na 3 kategorie np.: maly, sredni, wysoki 
pd.cut(txhousing['volume'],bins=3)
txhousing['city_contains_Abi']=txhousing['city'].str.contains('Abi').astype('int')
# wybiera 10 najwieksze
txhousing['sales'].nlargest(10)
# tworzy trzyliterowe skróty nazw miejscowosci ()
txhousing['city'].str.slice(stop=3).str.upper()
# zamieniay Abi na A
txhousing['city'].str.replace(pat='Abi',repl='A')
# robimhy split po spacjach 
txhousing['city'].str.split()
# znajduje a
txhousing['city'].str.find('a')

txhousing['sales>100']=(txhousing['sales']>100).astype('int')
txhousing.head()


salesmorethan100=[]
for row in txhousing['sales']:
    if row>100:
        salesmorethan100.append(1)
    else:
        salesmorethan100.append(0)

txhousing['salesmorethan100']=salesmorethan100
txhousing['sales'].where(txhousing['sales']<100,1)

txhousing.query('sales>100')
adult_data = pd.read_csv(
    "C:/Users/PawelEkk-Cierniakows/Downloads/adult.txt",
    names=[
        "Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Martial Status",
        "Occupation", "Relationship", "Race", "Sex", "Capital Gain", "Capital Loss",
        "Hours per week", "Country", "Target"],
        sep=r'\s*,\s*',
        engine='python')
adult_data.tail()

adult_data.info()
adult_data.shape

list(enumerate(adult_data.columns))

import numpy as np
import math
import matplotlib.pyplot as plt

fig=plt.figure(figsize=(20,15))
cols=5
rows=math.ceil(float(adult_data.shape[1])/cols)
for i,column in enumerate(adult_data.columns):
    ax=fig.add_subplot(rows,cols,i+1)
    ax.set_title(column)
    if adult_data.dtypes[column]==np.object:
        adult_data[column].value_counts().plot(kind='bar',axes=ax)
    else:
        adult_data[column].hist(axes=ax)
        plt.xticks(rotation='vertical')
plt.subplots_adjust(hspace=0.7,wspace=0.3)


for col in adult_data.columns:
    na_number=adult_data[col].isin(['?']).sum()
    if na_number>0:
        print(col)
        print(na_number)
        print("{0:.2f}%".format(na_number/adult_data.shape[0]*100))


adult_data=adult_data[adult_data['Workclass']!="?"]
adult_data=adult_data[adult_data['Occupation']!="?"]
adult_data=adult_data[adult_data['Country']!="?"]

adult_data.shape
quarters={'Jan':1,'Feb':1,'Mar':1}


try:
    x=int(input('Podaj liczb całkowitą: '))
    print(x)
except ValueError:
    print('Wpisana liczba nie jest całkowitą')


try:
    x=int(input('Podaj liczb całkowitą: '))
    print(x)
except TypeError:
    print('Wpisana liczba nie jest całkowitą')


try:
    x=int(input('Podaj liczb całkowitą: '))
    print(x)
except ValueError:
    print('Wpisana liczba nie jest całkowitą')
except TypeError:
    print('Wpisana liczba nie jest całkowitą')


try:
    x=int(input('Podaj liczb całkowitą: '))
    print(x)
except:
    print('Błąd')


