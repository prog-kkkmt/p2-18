#include <iostream>

using namespace std;

int main()
{
//Даны десять вещественных чисел. Найти их сумму.

       float a[10];// исходные данные
       for(int i = 0; i < 10; ++i){
        cin >> a[i];
       }
       float answer = 0.0; // ответ
       for(int i = 0; i < 10; ++i){
           answer+= a[i];//сложение и присвоениие ответа
       }
       cout << "answer = " << answer;// вывод
    }



