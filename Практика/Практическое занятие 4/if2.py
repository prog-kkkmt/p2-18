#Выполнил: Грушников К.С.
#https://stepik.org/lesson/189133/step/7?auth=login&unit=163636
#Stepik.Вам необходимо проанализировать введенное число
#0 <= n < 1000, и вывести"Число однозначное", "Число двузначное" или
#"Число трехзначное" в зависимости от длины числа. 
n = int(input())
if n < 10:
    print ("Число однозначное")
elif n < 100:
    print ("Число двузначное")
elif n < 1000:
    print ("Число трехзначное")