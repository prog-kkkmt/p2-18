#include <stdio.h>
#include <locale.h>
#include <windows.h>

void main ()
{
            setlocale(0,"");
    int mas[10], i, j, x=0, *pm;
        pm=&mas;
            printf ("Zapolnite massiv: ");
    for (i=0; i<10; i++)
        {
            scanf ("%d", pm);
            pm++;
        }
        pm-=10;
            printf ("\nMoy xyi: ");
    for (i=0; i<10; i++)
        {
            printf ("%d ", *pm);
            pm++;
        }
        pm-=10;
    for (i=0; i<9; i++)
        {
            if (*pm<*(pm+1))
            x=1;
            else
        {
        x=0;
            printf ("\nTvoi xyu%d", x);
        }
            pm++;
    }
    printf ("\nItogo %d", x);
}
