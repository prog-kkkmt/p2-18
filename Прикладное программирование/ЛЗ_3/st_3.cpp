/*
В коде программы определена следующая функция:
int foo(int n) {
    if (n <= 0)
        return 1;
    return foo((n * 2) / 3) + foo(n - 2);
}
Нужно посчитать, сколько всего раз будет вызвана функция foo,
если ее вызвать с аргументом 3 (т.е. foo(3)). Самый первый вызов тоже нужно посчитать.

Подсказка: для решения этой задачи будет полезно нарисовать дерево рекурсивных вызовов.
*/
#include <iostream>
using namespace std;
int i = 0;
int foo(int n)
{
    i ++;
    if (n <= 0)
        return 1;
    foo((n * 2) / 3) + foo(n - 2);
        return i;
}
int main()
{
    int n;
    cin >> n;
    cout << foo(n);
    return 0;
}
