#Слесарев А.М.

# Программист логирует программу, чтобы хорошо знать, как она себя ведет
#(эта весьма распространенная и важная практика).
#Он использует разные типы сообщений для вывода ошибок(error),
#предупреждений (warning), информации (info) или подробного описания (verbose). Сообщения отличаются по внешнему виду. Назовем модификаторами такие символы, которые отличают сообщения друг от друга, позволяя программисту понять, к какому из типов относится сообщения. Модификаторы состоят из двух одинаковых символов и записываются по разу в начале и в конце строки.
#@@ обозначает ошибку
#!! обозначает предупреждение
#// обозначает информационное сообщение
#** обозначает подробное сообщение
#Напишите программу, которая принимает строки до точки и выводит,
#какого типа это сообщение. Если сообщение не содержит модификаторов,
#проигнорируйте его.

err = list(input())
while err[0] != "." and a :
    a = len(err)
    if err[0] and err[1] and err[a-1] and err[a-2] == "@":
        print('ошибка')
    elif err[0] and err[1] and err[a-1] and err[a-2]  == "!":
        print('предупреждение')
    elif err[0] and err[1] and err[a-1] and err[a-2]  == "/":
        print('информация')
    elif err[0] and err[1] and err[a-1] and err[a-2]  == "*":
        print('подробное сообщение')
    err = list(input())
