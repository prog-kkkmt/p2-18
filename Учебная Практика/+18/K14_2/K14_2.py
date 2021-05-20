#Выполнил: Зайцев Никита
#Группа: П2-18
'''
К14_2. Техника работы с файлами

Задание 1. (Л.Б.)
При разработке курсовых проектов студентами 3 курса программистов ККМТ выбираются 
различные направления, например, "графика", "базы данных".. 
и предпочтения по языкам и средам "Си++", "Delphi"... 
В каждой строке текстового файла хранятся следующие сведения о курсовых проектах:
Фамилия Имя Отчество; Группа; Год; Тема; Направления (список через запятую); 
Языки и среды (список через запятую)

Например,
Иванов Иван Иванович;П1-21;2023;Картинки в базе;графика;Pascal,Lazarus

Программа должна читать входной файл и выдавать на экран ответы на вопросы
1. Какое направление встречается чаще всего
2. Какие языки и среды появились в дипломах в 2017 г.
'''

print()
fin = open("input.txt", 'r')
data_user = list()		#Список хранящий данные пользователей
num_user = 0			#Кол-во пользователей
keys_d = ['name', 'group', 'year', 'theme', 'direction', 'lang']	#Список названий (ключей) словаря
num_keys = len(keys_d)		#кол-во ключей

#Чтение файла и запись в список (data_user)
for str in fin:
	l = str.strip().split(';')	#Удаляем '\n' в конце и делим на части
	len_l = len(l)			#кол-во частей
	if (len_l != num_keys):
		print('Не достаточно данных')
		continue
	
	data_user.append(dict())	#Добавляем в список словарь, который будет хранить данные пользователя
	#Запись обычных данных (не многомерных)
	for i in range(len_l-2):
		data_user[num_user][keys_d[i]] = l[i]
	#Запись многомерных
	for i in range(len_l-2, len_l):
		data_user[num_user][keys_d[i]] = l[i].split(',')
	num_user += 1			#Кол-во пользователей
fin.close()

#Вывод данных о пользователях
for i in range(len(data_user)):	#Номер каждого человека
	print(f"---User #{i+1}---")
	for key in data_user[i]:
		print(f"{key}: {data_user[i][key]}")	#
	print()
print()


#--{1. Какое направление встречается чаще всего}--
d_dir = dict()			#Хранит имя_направления: кол-во_людей_которые_им_занимаются
pos_dir = -2			#Позиция "Направления" (direction) в списке ключей(keys_d)
for i in range(num_user):	#номер человека
	direct = data_user[i][keys_d[pos_dir]]	#Хранит список всех направлений человека
	for word in direct:
		d_dir[word] = d_dir.get(word, 0) + 1	#Подсчитываем кол-во каждого направления

num__d_dir = list(d_dir.values())	#Список кол-ва направлений каждого человека
maxx = max(num__d_dir)	#Наибольшее кол-во направлений
#Вывод наиболее часто встречающегося направления
print("Чаще всего встречается направление:", end=' ')
for i in d_dir:
	if (maxx == d_dir[i]):
		print(i, end=' ')
print('\n')


#--{2. Какие языки и среды появились в дипломах в 2017 г.}--
need_year = '2017'	#Год который мы ищем
lang = set()	#Множество хранящее языки и среды нужного нам года
pos_year = 2	#Позиция года в списке ключей(keys_d)
pos_lang = -1	#Позиция языков и сред в списке ключей(keys_d)
for i in range(len(data_user)):
	year = data_user[i][keys_d[pos_year]]	#Год пользователя
	if (year == need_year):
		set_lang = set(data_user[i][keys_d[pos_lang]])	#Хранит список всех языков и сред человека
		lang.update(set_lang)	#Объединяем множества "языков текущего пользователя" со "всеми языками пользователя" за нужный нам год
#Вывод
print("Языки и среды появившиеся в дипломах 2017 года:", end=' ')
print(*lang, sep=', ')


