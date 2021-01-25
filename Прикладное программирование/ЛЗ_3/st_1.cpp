/*
https://stepik.org/lesson/538/step/8?auth=login&unit=861
Напишите рекурсивную функцию вычисления наибольшего общего делителя двух положительных целых чисел 
(Greatest Common Divisor, GCD). Для этого воспользуйтесь следующими свойствами:

GCD(a, b) = GCD(b, a mod b)
GCD(0, a) = a
GCD(a, b) = GCD(b, a)
*/
#include <iostream>
using namespace std;
unsigned gcd(unsigned a, unsigned b)
{
    if (b!= 0)
    {
        return gcd (b, (a % b));
    }
    return a;
}
int main()
{
    int a, b;
    cin >> a >> b;
    cout << gcd(a, b);
    return 0;
}
