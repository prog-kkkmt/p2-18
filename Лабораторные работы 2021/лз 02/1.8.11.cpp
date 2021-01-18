//Выполнил задание: Пилипушко Андрей П2-18
//Задание: 1.8 Введение в синтаксис C++, часть 2
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int a, b, c, d;
    cin >> a >> b >> c;
    d = b * b - 4 * a * c;
    if (d > 0){
    cout << (-b - sqrt(d)) / (2 * a) << ' ';
    cout << (-b + sqrt(d)) / (2 * a);
    }
    else if (d == 0){
    d = -b / (2 * a);
    cout << d << ' ' << d;
    }
    else{
    cout << "No real roots";
    }

    return 0;
}
