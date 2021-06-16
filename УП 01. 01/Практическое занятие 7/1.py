# Выполнил: Короленко И.Р.
# Группы: П2-18

# С клавиатуры вводятся строки, последовательность заканчивается точкой.
# Выведите буквы введенных слов в верхнем регистре, разделяя их пробелами.
# Примечание: узнайте, как работает строковый метод upper().

word = input()
mass = []
while word != '.':
    mass.append(word)
    word = input()
for item in mass:
    output = ''
    for letter in item:
        output += letter.upper()
    print(*output)
