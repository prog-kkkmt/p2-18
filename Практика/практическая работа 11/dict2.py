# Выполнил задание Михайлов Данила
'''
Условие. В единственной строке записан текст. Для каждого слова из данного текста
подсчитайте, сколько раз оно встречалось в этом тексте ранее.
Словом считается последовательность непробельных символов идущих подряд, слова разделены
одним пробелом или символами конца строки.
'''
a = {}
sch = 1
for i in input().split():
    if i not in a:
        a.update({i:sch})
    else:
        a.update({i:a[i] + 1})
print(a)
