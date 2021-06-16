# 11_2_2 Слесарев А.М.
# Коля понял, что у многих из его знакомых есть несколько телефонных номеров и нельзя хранить только один из них.
# Он попросил доработать Вашу программу так, чтобы можно было добавлять к существующему контакту новый номер или
# даже несколько номеров, которые передаются через запятую. По запросу телефонного номера должен выводиться весь
# список номеров в порядке добавления, номера должны разделяться запятой. Если у контакта нет телефонных номеров,
# должна выводиться строка "Не найдено".
pb = dict()

data = input()
while data != '.':
    data = data.replace(',', '').split()
    if len(data) == 1:
        nm = ''.join(data)
        if nm in pb:
            print(', '.join(pb[nm]))
        else:
            print("Не найдено")
    else:
        nm, nmbr = data[0], data[1:]
        pb[nm] = pb.get(nm, []) + nmbr
    data = input()
