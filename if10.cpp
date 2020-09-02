#include <stdio.h>
int main(void)
{
   int a, b;

   scanf ("%d", &a); // Ввод A и B
   scanf ("%d", &b);

   if (a!=b) a=b=a+b; // Если а не равно b, то суммируем значение, если равны, то даем значениям 0
   else a=b=0;

   printf("a=%d\n b=%d\n",a,b); // вывод
   return 0;
}

