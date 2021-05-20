#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К13_1. Техника работы с кортежами

Задание 3. (Л.Б.) В каждой строке файла хранится информация о пунктах и их координатах
относительно некоторого центра.
Требуется
1. Прочесть файл в список кортежей
2. Найти диаметр множества точек, то есть расстояние между наиболее удалёнными точками. 
Указать наиболее удалённые пары
3. Сформировать список пар городов, имеющих одинаковое расстояние до центра
4. Отсортировать список одним из методов, реализованных в предыдущих работах
Результаты вывести на экран

Пример входного файла
Москва 0 0
Ивантеевка 20 15
Щёлково 10 30
Пушкино 15 5
'''

def BubbleSort(vals):
	n = len(vals)
	for i in range(n):
		for j in range(i+1, n):
			if (vals[i] < vals[j]):
				vals[i], vals[j] = vals[j], vals[i]
	return vals

fin = open("input.txt", 'r')
d_coord = dict()
d_hyp = dict()
print()
for str in fin:
	l = str.split()
	d_coord[l[0]] = tuple(l[1:])
	d_hyp[l[0]] = ( int(d_coord[l[0]][0])**2 + int(d_coord[l[0]][1])**2 )**0.5
fin.close()

vals_sort = BubbleSort(list(d_hyp.values()))

print("Сортированны по убыванию:")
numb_city = len(d_coord)
for i in range(numb_city):
	for city in d_hyp:
		if d_hyp[city] == vals_sort[i]:
			print(f"{i+1}|", end = ' ')
			print(city + ":", *d_coord[city], end = '\n   ')
			print(f"До центра: {int(vals_sort[i])} км\n")
			break

count = 0
for city_i in d_hyp:
	for city_j in d_hyp:
		if d_hyp[city_i] == d_hyp[city_j] and city_i != city_j:
			print(f"{d_hyp[city_i]} == {d_hyp[city_j]}")
			count += 1
if count == 0:
	print("Пар городов, имеющих одинаковое расстояние до центра, не обнаруженно")


'''
for i in sorted(d_hyp.values()):
	print(i)
'''

'''
fout = open("output.txt", 'w')
fout.write('\n'.join(tup))
fout.close()
'''
