# Выполнил: Бурлаев З.С.,Щепкин М.В. П2-18
# Programming Taskbook
# ЮФУ Электронный задачник по программированию
# М. Э. Абрамян (Южный федеральный университет), 1998–2020
# Case1. Дано целое число в диапазоне 1–7. Вывести строку —
# название дня недели, соответствующее данному числу
# 1 — «понедельник», 2 — «вторник» и т. д.).
day = ["понедельник","вторник","среда","четверг","пятница","суббота","воскресенье"]
a = int(input("Введите число 1-7:"))-1
print(day[a])
