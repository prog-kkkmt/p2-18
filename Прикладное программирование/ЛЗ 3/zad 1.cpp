/*https://stepik.org/lesson/538/step/8?unit=861*/

/*Напишите рекурсивную функцию вычисления наибольшего общего делителя двух положительных целых чисел
(Greatest Common Divisor, GCD). Для этого воспользуйтесь следующими свойствами:

GCD(a, b) = GCD(b, a \bmod b)GCD(a,b)=GCD(b,amodb)
GCD(0, a) = aGCD(0,a)=a
GCD(a, b) = GCD(b, a)GCD(a,b)=GCD(b,a)
 */

#include <iostream>

using namespace std;

unsigned gcd(unsigned a, unsigned b)
{
         if (b == 0)
                return a;
        return gcd(b, a % b);
}
/*Пример работы в программе*/
int main()
{
    int x, y;
    cin >> x;
    cin >> y;
    cout<<gcd(x, y)<<endl;

    return 0;
}
