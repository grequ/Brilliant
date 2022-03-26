import pandas as pd

filedirector = 'C:/Users/GrzegorzChuchra/Google Drive/machine learning/2. Praca z danymi w języku Python - Numpy i Pandas/'
txhousing=pd.read_excel(filedirector + 'txhousing.xlsx')
print(txhousing.head())


txhousing.assign(day=1)
# nie rozumeiem co ta lina ponizej robi. to assgine (day=1) wychodzi jakby robio date i usuwalo kolumen d
txhousing['date']=pd.to_datetime(txhousing[['year', 'month']].assign(day=1))
# txhousing['date']=pd.to_datetime(txhousing[['year', 'month','day']])
print(txhousing.head())
print (txhousing.groupby(['city','year']).agg(['sum','min','max'])['sales'])


# robimy nowa tabel gdzie agregujemy SALES po CITY, YEAR i pokazukujemy SUM, MIN, MAX
txhousing_agg=txhousing.groupby(['city','year']).agg(['sum','min','max'])['sales']
# nastepnie filtrujemy tylko po miesice 'abilene'
txhousing_agg.loc[['Abilene'],:]
# pozniej po miesice dla roku 2000 i wyzjej
txhousing_agg.loc[(['Abilene'],[2000]),:]
#  na koncu tylko dwa lata 2000 i 20001
print (txhousing_agg.loc['Abilene'].loc[2000:2001])

print(txhousing_agg.head())
txhousing_agg['sum'].nlargest(10)
txhousing_agg.to_excel(filedirector + 'txhousing_agg1.xlsx')
txhousing_agg=txhousing_agg.reset_index()
txhousing_agg.head()

txhousing_agg.to_excel(filedirector + 'txhousing_agg2.xlsx')
txhousing['day_name']=txhousing['date'].dt.day_name()
txhousing['month_name']=txhousing['date'].dt.month_name()

txhousing['days_in_month']=txhousing['date'].dt.days_in_month
txhousing['date1'] = txhousing['date'].dt.strftime('%m/%d/%Y')
txhousing['date2'] = txhousing['date'].dt.strftime('%d.%m.%Y')

txhousing=txhousing.rename({'days_in_month':'day'},axis=1)
txhousing.head()
txhousing['month_end'] = pd.to_datetime(txhousing[['year', 'month', 'day']])

txhousing['date']=txhousing['date'].dt.date
txhousing['month_end']=txhousing['month_end'].dt.date

txhousing.to_excel(filedirector + 'txhousing_preprocessed.xlsx')

########################################
# KOLEJNA CZĘŚĆ W PLIKU housing2.py
########################################


