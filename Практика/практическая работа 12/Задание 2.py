# https://pythontutor.ru/lessons/sets/problems/number_of_coincidental/
# Выполнил задание Михайлов Данила

'''
Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как
в первом списке, так и во втором.
'''
print(len(set(input().split()) & set(input().split())))
