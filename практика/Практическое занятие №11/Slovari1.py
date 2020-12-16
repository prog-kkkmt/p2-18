# Выполнил Толоконников Алексей Михайлович П2-18
# В единственной строке записан текст. Для каждого слова из данного текста подсчитайте,
# сколько раз оно встречалось в этом тексте ранее.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.

counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
