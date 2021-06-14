#Выполнил: Безбородов Константин
#Группа: П2-18
'''
К12_1. Техника работы с множествами

Задание 4. https://pythontutor.ru/lessons/sets/problems/number_of_words/
Задача «Количество слов в тексте»
Условие. Дан текст: в первой строке записано число строк, далее идут сами строки.
Определите, сколько различных слов содержится в этом тексте.
Словом считается последовательность непробельных символов идущих подряд, слова разделены
одним или большим числом пробелов или символами конца строки.
'''

words = set()
for i in range(int(input())):
    words.update(input().split())
print(len(words))