#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <locale.h>

int main()
{

setlocale(0,"");
int mas[10], i, j, x=0, B, sch=0, *pm, cvd, it, sch2=10;
pm=&mas;
printf ("Введите элементы: ");
for (i=0; i<10; i++)
{
scanf ("%d", pm);
pm++;
}
pm-=10;
printf ("Наш начальный массив: ");
for (i=0; i<10; i++)
{
printf ("%d ", *pm);
pm++;
}
pm--;
j=*pm;
printf ("\nПоследнее число: %d", j);
pm-=10;
for (i=0; i<10; i++)
{
cvd=(*pm)*(*pm);
sch2++;
if(cvd == j)
{
sch=i;
printf ("\nНайдено число: %d", *pm);
pm++;
printf ("\nНаш конечный массив: ");
for (i=sch; i<10; i++)
{
it=(*pm)*(*pm);
printf ("%d ", it);
pm++;
}
return 0;
}
pm++;
}
pm-=10;;
printf ("\nНаш конечный массив: ");
for (i=0; i<10; i++)
{
printf ("%d ", *pm);
pm++;
}
}
