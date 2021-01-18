//Выполнил задание: Пилипушко Андрей П2-18
//Задание: 1.8 Введение в синтаксис C++, часть 2

#include<iostream>

#define MAX(x, y, r) {typeof(x) _x = x; typeof(y) _y = y; (r) = (_x > _y ? _x : _y);}
