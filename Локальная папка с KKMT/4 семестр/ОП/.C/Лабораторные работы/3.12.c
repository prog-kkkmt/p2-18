#include <stdio.h> 
#include <locale.h> 
#include <time.h> 

void main() 
{ 
		setlocale(0,""); 
	srand(time(NULL)); 
int n, i, *pm, B, x=0, mest; 
		printf ("Введите размер массива: ");  
	scanf ("%d", &n);
int mas[n];
	pm=&mas;
for (i=0; i<n; i++)
	{
		*pm=rand()%100-50;
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
printf ("Введите число: ");
scanf ("%d", &B);
for (i=0; i<n; i++)
{
	if (*pm==B)
	{
		x=1;
		mest=i+1;
		break;
	}
	pm++;
}
pm-=mest;
for (i=0; i<mest; i++)
{
	if (*pm!=0)
	{
		x*=*pm;
	}
	pm++;
}
printf ("Результат: %d", x);
}

