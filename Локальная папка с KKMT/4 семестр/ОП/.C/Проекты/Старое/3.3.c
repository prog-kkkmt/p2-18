#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <locale.h>

int main()
{

setlocale(0,"");
int mas[10], i, j, x=0, B, sch=0, *pm, cvd, it, sch2=10;
pm=&mas;
printf ("������� ��������: ");
for (i=0; i<10; i++)
{
scanf ("%d", pm);
pm++;
}
pm-=10;
printf ("��� ��������� ������: ");
for (i=0; i<10; i++)
{
printf ("%d ", *pm);
pm++;
}
pm--;
j=*pm;
printf ("\n��������� �����: %d", j);
pm-=10;
for (i=0; i<10; i++)
{
cvd=(*pm)*(*pm);
sch2++;
if(cvd == j)
{
sch=i;
printf ("\n������� �����: %d", *pm);
pm++;
printf ("\n��� �������� ������: ");
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
printf ("\n��� �������� ������: ");
for (i=0; i<10; i++)
{
printf ("%d ", *pm);
pm++;
}
}
