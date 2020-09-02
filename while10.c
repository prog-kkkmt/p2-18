#include <stdio.h>
int main(void)
{
   int n;
   printf("n=");

scanf ("%i", &n); //ввод n

int k=0, a=3;
   while (a<n) { // вводим в степень
        a*=3;
        ++k;
   }
   printf("k= %i\n",k); // вывод k

   return 0;
}
