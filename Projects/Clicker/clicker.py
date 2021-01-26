# Крайне простой кликер для убийства времени на скучных парах (коими являются все, кроме пар Леонида Борисовича :D)

import readchar

string = 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z'
print('Можно нажимать только на английской раскладке. Регистр не важен.')
print('q - Выход из кликера.')
n = 0
secret_key = 0
while n >= 0:
    key = readchar.readkey()
    if any((key in string) for key in string) == 1:
        n += 1
        print('Good boiiii! Держи балл!\n' + str(n))
        if key == 'q':
            print('Наигрался, да? Ну и ладно ;c\nВыход из кликера...')
            break
        if key == 'o':
            secret_key += 1
            if secret_key >= 10:
                print('Ого, ты несколько раз нажал на секретную кнопку?! Красава! Держи 100 очков!')
                secret_key -= 999999999999
                n += 100