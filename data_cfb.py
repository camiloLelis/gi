import datetime
import os
os.system('clear')
nasc= datetime.datetime(2018,9,17)
nasceu=datetime.date(2010,4,28)
data= datetime.datetime.now()
print (str(data.day) + "/" + str(data.month) + "/" + str(data.year))
print (data)
x= data-nasc
d=x/365
print(x)
print(d)
print (nasceu)