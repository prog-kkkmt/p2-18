#Выполнил: Короленко Иван Романович
#Студент: П2-18

'''
Задача «Самое частое слово»
Условие. Дан текст: в первой строке задано число строк, далее идут сами строки. 
Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, 
выведите то, которое меньше в лексикографическом порядке.
'''

word = {}
for i in range(int(input())):
    line = input().split()
    for words in line:
        word[words] = word.get(words, 0) + 1
         
count = max(word.values())
most_frequent = [k for k, v in word.items() if v == count]
print(min(most_frequent))

#Более простой вариант 
word = {}
for i in range(int(input())):
    for words in input().split():
        word[words] = word.get(words, 0) + 1

for i in sorted(word.items(), key=lambda x: (x[0])):    
    if i[1] == max(word.values()):
        print(i[0])
        break
