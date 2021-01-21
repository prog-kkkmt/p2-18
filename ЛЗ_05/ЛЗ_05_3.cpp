/*Напишите функцию поиска первого вхождения шаблона в текст.
В качестве первого параметра функция принимает текст (C-style строка),
в которой нужно искать шаблон. В качестве второго параметра строку-шаблон
(C-style строка), которую нужно найти. Функция возвращает позицию первого
вхождения строки-шаблона, если он присутствует в строке (помните, что в C++
принято считать с 0), и -1, если шаблона в тексте нет.

Учтите, что пустой шаблон (строка длины 0) можно найти в любом месте текста.

Требования к реализации: при выполнении данного задания вы можете определять
любые вспомогательные функции, если они вам нужны. Вводить или выводить
что-либо не нужно. Реализовывать функцию main не нужно
Сделал: Сумин К.Е. Группа П2-18*/
#include <iostream>


using namespace std;


int trigger=-1,temp=-1,chet=0;
int strst(const char *text, const char *pattern)
{
    temp++;
    if (trigger==-1)
    {
        chet=0;
    }
    if (*pattern=='\0')
    {
        if(chet==0)
        {
            return 0;
        }
        return trigger;
    }
    if(*text==*pattern)
    {
        if (trigger==-1)
        {
            trigger=temp;
        }
        chet++;
        strst(text+1,pattern+1);
    }
    else
    {
        if (trigger!=-1)
        {
            int junk=trigger,rubbish=temp;
            trigger=-1;
            temp=temp-chet;
            strst(text-rubbish+junk+1,pattern-chet);
        }
        else
        {
            if ((*text=='\0')&&(trigger==-1))
            {
                if((chet==0)&&(*pattern=='\0'))
                {
                    return temp;
                }
                return trigger;
            }
            strst(text+1,pattern-chet);
        }
    }
}


int main()
{
    char a[10] = {'a','s','a','s','a','f','\0'};
    char b[10] = {'a','s','a','f','\0'};
    char *aa=&a[0],*bb=&b[0];
    cout<<strst(aa,bb);
    return 0;
}