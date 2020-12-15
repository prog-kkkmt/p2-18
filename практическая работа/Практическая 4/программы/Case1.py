x = int(input())
if 0 < x < 8:
    if x == 1:
        print("Понедельник")
    elif x == 2:
        print("Вторник")
    elif x == 3:
        print("Среда")
    elif x == 4:
        print("Четверг")
    elif x == 5:
        print("Пятница")
    elif x == 6:
        print("Суббота")
    elif x == 7:
        print("Воскресенье!")
else:
    print("Число не в диапазоне")
