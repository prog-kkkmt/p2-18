//ƒаны три целых числа. Ќайти количество положительных чисел в исходном наборе.
#include <iostream>
#include <time.h>
#include <stdlib.h>

using namespace std;

int main()
{
int a, b, c, flag;
cin >> a >> b >> c;
if (a > 0){
flag +=1;
}
if (b > 0){
flag +=1;
}
if (c > 0){
flag +=1;
}	
cout << flag;



return 0; // возвращаем 0
}
