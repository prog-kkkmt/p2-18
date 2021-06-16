//Выполнили: Короленко И.Р., Кузнецов М.С., Слесарев А.М.
//Группа: ККМТ П2-18
//Задание: 2.2 Стек вызовов

#include <iostream>

using namespace std;

void rev()
{
    int a = 0;
    cin >> a;
    if(a == 0) return;
        rev();
    cout << a << " ";
}
int main()
{
    rev();
    return 0;
}
