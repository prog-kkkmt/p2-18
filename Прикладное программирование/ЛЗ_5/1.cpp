//https://stepik.org/lesson/540/step/6?unit=863
/*
Очень часто для работы со строками нам нужно сначала вычислить длину строки. Для C-style строк длина нигде явно не хранится, но её можно вычислить. Напишите функцию, которая вычисляет длину C-style строки. Учтите, что завершающий нулевой символ считать не нужно.
*/
#include <iostream>
using namespace std;
unsigned strlen(const char *str)
{
    int a = 0;
    while (str[a] != '\0')
    {
        a ++;
    }
    return a;
}
int main()
{
    const char *str = "C style";
    cout << strlen (str);
return 0;
}