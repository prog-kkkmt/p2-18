# Выполнил Кузнецов М. С. П2-18.
# Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.

print(len(set(input().split()) & set(input().split())))
