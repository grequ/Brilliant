import numpy as np

roi = np.array([ 1.25,  3.75, 10.  , 20.  ,  0.4 ])
filename = 'C:/Users/GrzegorzChuchra/Google Drive/machine learning/2. Praca z danymi w języku Python - Numpy i Pandas/tablica.txt'
np.savetxt(filename,roi,delimiter=',')

odczytpliku=np.loadtxt(filename)
print(odczytpliku)


tbl_zeros = np.zeros((3,2), dtype=int)

# zadanie - symulacja dużego lotka 

#number from 0-48

tbl_BigLottery = np.random.randint(49, size=(1, 6))
print(tbl_BigLottery)


# for iterator in range(tbl_BigLottery):
#     currentIterator = 0

#     for subiterator in range(tbl_BigLottery):
#         if iterator != subiterator:







# jaka jest szansa trafienia w 1,000,000 powtorzen