#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <locale.h>
#include <time.h>

void main ()
{
                srand(time(NULL));
    setlocale(0,"");
            int mas[10], i, j, x=0, B, sch=0, *pm;
                pm=&mas;
        for (i=0; i<10; i++)
            {
                *pm=rand()%100-50;
                pm++;
            }
        pm-=10;
                printf ("Массив: ");
        for (i=0; i<10; i++)
                {
                    printf ("%d ", *pm);
                    pm++;
                }
        pm-=10;
                printf ("\nВведите число=");
    scanf ("%d", &B);
        for (i=0; i<10; i++)
            {
                if(*pm == B)
            {
                j=i;
                break;
            }
        pm++;
            }
        pm-=j;
                    if (j==-1)
            {
                printf("...: %d", x);

            }
else
        {
    for (i=0; i<j; i++)
        {
            if (*pm>=0 && *pm%2==0)
            x+=*pm;
        pm++;
        }
}
printf("Сумма: %d", x);
}
