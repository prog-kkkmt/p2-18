#Выполнил Кузнецов М. С. П2-18.
#Улитка ползет по вертикальному шесту высотой h метров,
#поднимаясь за день на a метров, а за ночь спускаясь на b метров.
#На какой день улитка доползет до вершины шеста?
#Программа получает на вход натуральные числа h, a, b.
#Программа должна вывести одно натуральное число. Гарантируется, что a > b.
h, a, b = int(input()), int(input()), int(input())
print(int(1 + (h - b - 1) / (a - b)))
