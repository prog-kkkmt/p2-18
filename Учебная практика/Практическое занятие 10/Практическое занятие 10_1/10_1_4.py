#http://ptaskbook.com/ru/tasks/func.php
#Func33
#Выполнили: Воронцов А.А. Бурлаев З.С. Щепкин М.В. П2-18

"""
Описать функцию SortInc3(X), меняющую содержимое списка X из трех 
вещественных элементов таким образом, чтобы их значения оказались упорядоченными по 
возрастанию (функция возвращает None). С помощью этой функции упорядочить по 
возрастанию два данных списка X и Y.
"""
def SortInc3(X):
    return sorted(X)

x = [int(input()) for i in range(3)]
y = [int(input()) for j in range(3)]
print(SortInc3(x))
print(SortInc3(y))
