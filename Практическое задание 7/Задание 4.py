# Выполнил Зайцев Н. Е. П2-18.
# @@ обозначает ошибку
# !! обозначает предупреждение
# // обозначает информационное сообщение
# ** обозначает подробное сообщение
# Напишите программу, которая принимает строки до точки и выводит, 
# какого типа это сообщение. Если сообщение не содержит модификаторов, 
# проигнорируйте его.
def log(msg =''): # Делаем функцию
    if len(msg) >= 2:
        type_ = msg[0]+msg[1]
        if type_ == '!!': # Если в переменное есть значение, то вывести print
            print ('предупреждение') 
            return
        if type_ == '@@':
            print ('ошибка') 
            return
        if type_ == '//':
            print ('информация') 
            return
        if type_ == '**':
            print ('подробное сообщение') 
            return


log(input('write: ')) # Вызов функции
