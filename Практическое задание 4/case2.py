#Выполнил Зайцев Н. Е. П2-18.
#Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — 
#февраль и т. д.). Определить количество дней в этом месяце для 
#невисокосного года.

a = int(input("Введите номер месяца: "))
if 0 < a < 13:
    if a == 1:
        print("январь, 31 день")
    elif a == 2:
        print("февраль, 28 дней")
    elif a == 3:
        print("март, 31 день")
    elif a == 4:
        print("апрель, 30 дней")
    elif a == 5:
        print("май, 31 день")
    elif a == 6:
        print("июнь, 30 дней")
    elif a == 7:
        print("июль, 31 день")
    elif a == 8:
        print("август, 31 день")
    elif a == 9:
        print("сентябрь, 30 дней")
    elif a == 10:
        print("октябрь, 31 день")
    elif a == 11:
        print("ноябрь, 30 дней")
    elif a == 12:
        print("декабрь, 31 день")
else:
    print("Ошибка")

