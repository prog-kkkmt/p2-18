#Выполнил задание Михайлов Данила
#программа которая выбирает случайные(пронумерованные по сложности задания )
#и создает 7 билетов в которых по 5 заданий
from random import *
s = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10', 'b11', 'b12', 'b13', 'b14', 'b15', 'b16', 'c17',
          'c18', 'c19', 'c20']
b = []
gb = []
for i in range(7):
    for x in range(5):                  
        e = randint(0,19)               
        b.append(s[e])        
    gb.append(billet)        
    b = []                         
print(gb)     
