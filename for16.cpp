// Дано вещественное число A и целое число N (> 0).
//Используя один цикл, вывести все целые степени числа A от 1 до N.
#include <iostream>
using namespace std;

int main()
{
    float a;
    cout << "A:";
    cin >> a;

   int b;
   cout << "b:";
   cin >> b;

   float c=1;
   int i;
   for  (i =1; i<=b; ++i){
      c *= a;
     cout << c << endl;
   }
   return 0;
}
