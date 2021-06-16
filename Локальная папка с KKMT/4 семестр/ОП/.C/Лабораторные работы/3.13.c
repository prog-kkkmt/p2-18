#include <stdio.h> 
#include <locale.h> 

void main() 
{ 
		setlocale(0,""); 
	srand(time(NULL)); 
int n, i, *pm, mest, x=0, sum, sch=0; 
			printf ("Введите размер массива: ");  
		scanf ("%d", &n);
int mas[n];
pm=&mas;
for (i=0; i<n; i++)
{
	scanf ("%d", pm);
	pm++;
}
pm-=n;
printf ("Наш массив: "); 
for (i=0; i<n; i++) 
{ 
	printf ("%d ", *pm); 
	pm++; 
} 
pm-=n;
for (i=0; i<n; i++)
{
	if (*pm==0)
	{
		x=1;
		mest=i+1;
		break;
	}
	pm++;
}
pm-=mest;
if (x==1)
{
for (i=0; i<mest; i++)
{
	if (*pm>0)
	{
		sum+=*pm;
		sch++;
	}
	pm++;
}
printf ("\nCумма: %d, Коллич: %d", sum, sch);
}
else
printf ("\nНулевых элементов нет");
}
