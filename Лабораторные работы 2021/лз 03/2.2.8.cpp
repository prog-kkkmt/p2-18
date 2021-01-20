//Выполнил задание: Пилипушко Андрей П2-18
/*Задание: Напишите рекурсивную функцию вычисления наибольшего общего делителя двух положительных целых чисел
  (Greatest Common Divisor, GCD).*/

#include <iostream>

unsigned gcd(unsigned a, unsigned b)
{
   if(b==0)
       return a;
   return gcd(b,a%b);
}
int main(){
 int a, b;
std::cin >> a >> b;
std::cout << gcd(a, b);
 return 0;
}
