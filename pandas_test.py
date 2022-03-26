import pandas as pd
import numpy as np

#zadanie 0


# df = pd.DataFrame([[np.nan, 2, np.nan, 0], [3, 4, np.nan, 1], [np.nan, np.nan, np.nan, np.nan], [np.nan, 3, np.nan, 4]], columns=list("ABCD"))
# print (df)
# df.fillna(0)
# print (df)
# df.fillna(0,inplace=True)
# print (df)
# # workshope with pawel





# zadanie 2

filename = 'C:/Users/GrzegorzChuchra/Google Drive/machine learning/2. Praca z danymi w języku Python - Numpy i Pandas/hitters.csv'

hitters=pd.read_csv(filename)


hitters.boxplot('Salary')
#wybierze mi te hitters gdzie Division jest równe W
gf = hitters[hitters['Division'] == 'W']

print(gf.head())

# hitters.head()
# hitters.info()

# print (hitters['Salary'].mean())
# print (hitters['Salary'].median())
# print (hitters['Salary'].min())
# print (hitters['Salary'].sum())
# print (hitters['Salary'].max())
# print (hitters['Assists'].quantile([.01,.25,.5,.75,.99]))

# print(hitters.describe())

# print (hitters['Division'].value_counts())
# print ("")

# print (hitters.groupby('Division').Assists.mean())
# print ("")

# print (hitters.groupby('Division').Salary.mean())
# print (hitters.groupby('Division').Salary.min())
# print (hitters.groupby('Division').Salary.sum())
# print (hitters.groupby('Division').Salary.max())

print (hitters.groupby('Division').Salary.count())
print (hitters.Division.value_counts())
print (hitters.groupby('Division').count())

# hitters with salary above the median
hittersMedian = hitters['Salary'].median()
hitters['IsAboveMedian'] = hitters['Salary'] > hittersMedian
hitters['Salaryovermedian']=(hitters['Salary']>hittersMedian).astype('int') # the same as above but with convertion to the INT from Bool 
print (hitters.head())

print (np.corrcoef(hitters['Salaryovermedian'],hitters['Assists'])[0,1])
print (hitters.corr())


#zadanie - obrazki

hitters.boxplot('Salary')
hitters.boxplot()
hitters.boxplot(column='Salary',by='Division')
hitters.groupby('Division').Salary.plot(kind='hist',bins=5,legend=True,alpha=0.4)


for column in ['League','Division','NewLeague']:
    print(hitters.groupby(column).Salaryovermedian.mean())

# percAboveMedian = hitters.groupby('Division').Salary.mean() / hitters.groupby('Division').Salary.mean()
# print("The percentage of players with salary above median = " + percAboveMedian)



# next set of operaton

# what is index: https://www.w3resource.com/pandas/dataframe/dataframe-set_index.php
# hitters.set_index('Unnamed: 0')
# hitters=hitters.drop('Unnamed: 0',axis=1)


# generate random dictionary

dictionary={'a':np.random.randint(100,size=10),'b':np.random.randint(100,size=10)}

print (dictionary)

df = pd.DataFrame(dictionary)
df['c'] = df['a'] + df['b']
df['d'] = df['c'] > 100
df['e'] = 'text'
del df['e']

#set of functions

# hitters.fillna(hitters.Salary.mean()).info()
