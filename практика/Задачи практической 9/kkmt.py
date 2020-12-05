kkmt=[]
kod=[]
file = open('name.txt', encoding='utf-8')
name=list(tuple(item.replace('\n', '') for item in line.split(' ')) for line in file)
for i in range(0,len(name),+1):
    if kod.count(name[i][1]) == 0:
        kod.append(name[i][1])
for i in range(0,len(kod),+1):
    for j in range(0,len(name),+1):
        temp=0
        while temp<3:
            if name[j][1] == kod[i] and temp==0 and name[j][2=='coder'] and kkmt.count(name[j])!=name.count(name[j]):
                kkmt.append(name[j])
                temp+=1
            elif name[j][1] == kod[i] and temp==1 and name[j][2=='designer'] and kkmt.count(name[j])!=name.count(name[j]):
                kkmt.append(name[j])
                temp += 1
            elif name[j][1] == kod[i] and temp==2 and name[j][2=='tester'] and kkmt.count(name[j])!=name.count(name[j]):
                kkmt.append(name[j])
                temp += 1
            elif name[j][1] == kod[i] and temp==3 and name[j][2=='writer'] and kkmt.count(name[j])!=name.count(name[j]):
                kkmt.append(name[j])
                temp += 1
            else:
                temp=4
try:
    n=0
    pr=0
    bug=0
    aaa=0
    for j in range(0,len(kod),+1):
        coun=1
        temp=0
        for k in range (0,len(kkmt),+1):
            temp+=kkmt[k].count(kod[j])
        if temp/4!=0:
            coun=int(temp/4)
        if coun==1:
            for i in range(n,n+temp,+1):
                if bug%4==0:
                    print("Команда №",int(pr/4)+1)
                print(kkmt[i])
                pr += 1
                aaa += 1
                if bug!=3:
                    bug+=1
                else:
                    bug=0
        else:
            for i in range(n, n + temp, +1):
                if bug%4==0 and i%2!=0:
                    print("Команда №",int(pr/4)+1)
                if i%2!=0:
                    print(kkmt[i])
                    pr += 1
                    aaa += 0.5
                    if bug != 3:
                        bug += 1
                    else:
                        bug = 0
            for i in range(n, n + temp, +1):
                if bug%4==0 and i%2==0:
                    print("Команда №",int(pr/4)+1)
                if i%2==0:
                    print(kkmt[i])
                    pr+=1
                    aaa += 0.5
                    if bug != 3:
                        bug += 1
                    else:
                        bug = 0
        n+=temp
    if aaa!=len(kod)*4:
        print("Всязи с недостатком участников, некоторые команды были сформированы некорректно\n"
              "Пожалуйста, уберите участников которым не хватает людей для команды, или найдите\n"
              "им людей в команду")
except:
    print("Всязи с недостатком участников, некоторые команды были сформированы некорректно\n"
    "Пожалуйста, уберите участников которым не хватает людей для команды, или найдите\n"
    "им людей в команду")
