//https://stepik.org/lesson/Стек-вызовов-538/step/9?unit=861
/*
В коде программы определена следующая функция:

int foo(int n) {
    if (n <= 0)
        return 1;
    return foo((n * 2) / 3) + foo(n - 2);
}
Нужно посчитать, сколько всего раз будет вызвана функция foo, если ее вызвать с аргументом 3 (т.е. foo(3)). Самый первый вызов тоже нужно посчитать. 
*/
#include <iostream>
using namespace std;
int foo(int n) 
    {
    if (n <= 0)
        return 1;
    return foo((n * 2) / 3) + foo(n - 2);
    }
// Функция foo будет вызвана 9 раз
