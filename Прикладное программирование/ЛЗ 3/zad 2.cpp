/*https://stepik.org/lesson/538/step/9?unit=861*/

/*В коде программы определена следующая функция:

int foo(int n) {
    if (n <= 0)
        return 1;
    return foo((n * 2) / 3) + foo(n - 2);
}
Нужно посчитать, сколько всего раз будет вызвана функция foo, если ее вызвать с аргументом 3 (т.е. foo(3)).
 Самый первый вызов тоже нужно посчитать.

*/

#include <iostream>

using namespace std;

// функция foo будет вызываться 9 раз, чтобы в этом убедиться сделаем глобальныую переменную cnt со счётчиком и посчитаем в программе:

extern int cnt = 0;

int foo(int n) {
    cnt ++;
    if (n <= 0)
        return 1;
    return foo((n * 2) / 3) + foo(n - 2);

}
int main()
{
    int n = 3;
    cout << foo(n) << endl;
    cout << cnt << endl;

    return 0;
}
