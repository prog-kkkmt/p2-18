//8Даны два числа. Вывести вначале большее, а затем меньшее из них.
#include <stdio.h>

int main(void)
{
   int a1, a2;
   printf("a1:");
   scanf ("%i", &a1);
   printf("a2:");
   scanf ("%i", &a2);

    if (a1>a2) printf(" %i %i\n",a1, a2);
   else printf(" %i %i\n",a2, a1);

    return 0;
}
