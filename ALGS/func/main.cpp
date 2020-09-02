#include <iostream>

//Описать функцию Sign(X) целого типа, возвращающую для вещественного числа X следующие значения:
//−1,    если X < 0;        0,    если X = 0;        1,    если X > 0.
//С помощью этой функции найти значение выражения Sign(A) + Sign(B) для данных вещественных чисел A и B.
using namespace std;

int Sign(float x){ //функиця Sign по заданию

    if(x < 0){
        return -1;
    }
    else if(x == 0){
        return 0;
    }
    else{
        return 1;
        }

    };

int main()
{
float a, b; //исходные данные
cin >> a;
cin >> b;
cout << "answer = "<<  Sign(a) + Sign(b);// вывод
}



