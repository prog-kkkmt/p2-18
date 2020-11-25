#include <stdio.h>
int main(void)
{
   int n, k=0, a=3;
   printf("n=");

scanf ("%i", &n); //ââîä n

   while (a<n) { // ââîäèì â ñòåïåíü
        a*=3;
        ++k;
   }
   printf("k= %i\n",k); // âûâîä k

   return 0;
}
