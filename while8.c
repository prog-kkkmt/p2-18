//Дано целое число N (> 0). Найти наибольшее целое число K, квадрат которого не превосходит N: K2 ≤ N.
//Функцию извлечения квадратного корня не использовать.
#include<stdio.h>
int main(void)
{
   int n;
   printf("N:");
   scanf ("%i", &n);
   int k=1;
   while (k*k<=n) ++k;
   printf("K: %i\n",k);
   return 0;
}
