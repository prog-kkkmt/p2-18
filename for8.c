//Даны два целых числа A и B (A < B). Найти произведение всех целых чисел от A до B включительно.
#include <stdio.h>
int main(void)
{
   int a,b;
   printf("A:");
   scanf ("%i", &a);

   printf("B:");
   scanf ("%i", &b);

   int i, rez=1;
    for  (i =a; i<=b; ++i)
      rez *=i;
   printf("rez = %i \n ",rez);

   return 0;
}
