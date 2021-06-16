#include <windows.h>
#include <stdio.h> 
#include <locale.h> 

void main() 
{ 
		setlocale(0,""); 
	srand(time(NULL)); 
int a, b, i, sum, j, sch=0,*pm,x=0; 
			printf ("Введите размер массива: ");  
		scanf ("%d", &a);
		printf ("Введите число:");
		scanf ("%d",&b);
int mas[a];
pm=&mas;
for (i=0; i<a; i++)
{
	scanf ("%d", pm);
	pm++;
}
pm-=a;
printf ("Наш массив: "); 
for (i=0; i<a; i++) 
{ 
	printf ("%d ", *pm); 
	pm++; 
} 
pm-=a;
for (i=0; i<a; i++)
{
	if (*pm==b)
	{
		x=1;
		j=i+1;
		break;
	}
	pm++;
}
pm-=j;
if (x==1)
{
for (i=0; i<j; i++)
{
	if (*pm>0 && *pm%2==0)
	{
		sum+=*pm;
		sch++;
	}
	pm++;
}
printf ("\nCумма: %d, Коллич: %d", sum, sch);
}

}
