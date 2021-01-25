//https://stepik.org/lesson/Стек-вызовов-538/step/8?unit=861
/*Напишите рекурсивную функцию вычисления наибольшего общего делителя двух положительных целых чисел (Greatest Common Divisor, GCD). 
Для этого воспользуйтесь следующими свойствами:
1.GCD(a,b) = GCD(b,amodb)
2.GCD(0, a) = aGCD(0,a) = a
3.GCD(a, b) = GCD(b, a)
Требования к реализации: в данном задании запрещено пользоваться циклами. Вы можете заводить любые вспомогательные функции, если они вам нужны.
Функцию main определять не нужно.
*/
#include <iostream>
using namespace std;
int gcd (int a, int b)
{
    if(b == 0)
         return a;
    else
         return gcd (b, a % b);
         
}
    int main()
    {
        int a,b;
        cin >> a >> b;
        cout << gcd(a,b);
        return 0;
    }
