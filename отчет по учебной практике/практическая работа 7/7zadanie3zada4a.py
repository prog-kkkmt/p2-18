x = 'VSEM PRIVET, ETO ZASHITA OT CAPSLOKE' #строка в верхнем регистре
if x.isupper() == True:                    #проверка на верхний регистр
    x = x.capitalize()                     #переводит в верхний регистр первую букву только самого первого слова строки
print(x)                                   #вывод строки