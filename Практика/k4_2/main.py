def day(data,bol):
    uni = {
        0: '',
        1:'первое',
        2:'второе',
        3:'третье',
        4:'четвертое',
        5:'пятое',
        6:'шестое',
        7:'седьмое',
        8:'восьмое',
        9:'девятое',
    }
    if int(data)<10:
        if bol == 1:
            return str(uni[int(data)][:-1]+'го')
        return uni[int(data)]
    elif int(data)<20:
        doz = {
            10:'десятое',
            11:'один',
            12:'две',
            13:'три',
            14:'четыр',
            15:'пят',
            16:'шест',
            17:'сем',
            18:'восем',
            19:'девят'
        }
        if bol == 1:
            if int(data) == 10:
                return str(doz[data][:-1] + 'го')
            return str(doz[data]+'надцатого')
        elif int(data) == 10:
            return doz[int(data)]
        else:
            return str(doz[int(data)]+'надцатое')
    else:
        doz = {
            2:'двадцать',
            3:'тридцать',
            4:'сорокок',
            5:'пятьдесят',
            6:'шестьдесят',
            7:'семьдесят',
            8:'восемдесят',
            9:'девяносто'
        }
        if bol == 1 and int(data)%10 == 0:
            if str(doz[int(data)//10][-1:]) == 'ь' or str(doz[int(data)//10][-1:]) == 'о':
                return str(doz[int(data) // 10][:-1]+'ого')
            return str(doz[int(data)//10]+'ого')
        return str(doz[int(data)//10]+' '+day(int(data)%10,bol))



def month(data):
    mon = {
        1:'января',
        2:'февраля',
        3:'марта',
        4:'апреля',
        5:'мая',
        6:'июня',
        7:'июля',
        8:'августа',
        9:'сентября',
        10:'октября',
        11:'ноября',
        12:'декабря'
    }
    return mon[int(data)]


def year(data):
    tho = {
        0:'',
        1:'одна тысяча',
        2:'две тысячи',
        3:'три тысячи'
    }
    hun = {
        0:'',
        1:'сто',
        2:'двести',
        3:'триста',
        4:'четыреста',
        5:'пятьсот',
        6:'шестьсот',
        7:'семьсот',
        8:'восемьсот',
        9:'девятьсот'
    }
    if int(data)%100 == 0:
        if str(hun[int(data) % 1000 // 100][-1:]) != 'т':
            junk = {
                1:'',
                2:'двух',
                3:'трех',
                4:'четырех'
            }
            if int(data)%1000 == 0:
                if int(data)%10000 == 0:
                    return 'Jesus'
                return str(junk[int(data) // 1000]+'тысечного')
            return str(tho[int(data) // 1000] + ' ' + str(junk[int(data) % 1000 // 100]+'сотого'))
        return str(tho[int(data) // 1000] + ' ' + hun[int(data) % 1000 // 100]+'ого')
    return str(tho[int(data)//1000]+' '+hun[int(data)%1000//100]+' '+str(day(int(data)%100,1)))

file=open('data.txt',"r")
print(day(file.read(2),0), month(file.read(3)[1:]), year(file.read()[1:]))
file.close()