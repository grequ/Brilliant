import numpy as np



# zadanie 2

y = []

for x in range(11):
    if x%2 == 0:
        y.append(x)

print (y)
print (type(y))

z = np.array(y)
print (z)
print (type(z))


print(np.arange(0,11,2))
print(np.linspace(0,10,5))
print(np.linspace(1,10,5))
print(np.linspace(0,10,6))


# zadanie 1

net_income=[100,150,300,400,40]
investment=[80,40,30,20,100]

np_net_income = np.array(net_income)
np_investment = np.array(investment)

roi = net_income + investment
roi_2 = np_investment + np_net_income

print (roi)
print (type(roi))

print (roi_2)
print (type(roi_2))


# zadanie 3

tablica = np.array([net_income,investment])

