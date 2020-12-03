#Выполнил: Короленко Иван Романович
#Студент: ККМТ П2-18

#Задание 3
#Text20. Дан текстовый файл.
#Заменить в нем все подряд идущие пробелы на один пробел.

file1 = "text20.txt"
print("Read from:",file1)
file2 = "text20_2.txt"
print("Write to:",file2)

flag = True
try:
    with open(file1, 'r') as infile, open(file2, 'w') as outfile:
        for line in infile:
            line_new = ""
            print(line)
            for c in line.strip("\n"):
                if c != " ":
                    line_new += c
                    flag = True
                elif flag:
                    line_new += c
                    flag = False
            outfile.write(line_new+"\n")
            

except IOError:
    print('Open error: ',file1)

