//Выполнили: Короленко И.Р., Кузнецов М.С., Слесарев А.М.
//Группа: ККМТ П2-18
//Задание: 1.8 Введение в синтаксис C++, часть 2

#include <iostream>
#define MAX(a,b,c) ( (a) > (b) ? (c = a) : (c = b) )

using namespace std;

int main(){
    int a = 10;
    int b = 20;
    int c = 0;
    cout « MAX(a, b, c) « endl;
    cout « MAX(a += b, b, c);
    return 0;
}

