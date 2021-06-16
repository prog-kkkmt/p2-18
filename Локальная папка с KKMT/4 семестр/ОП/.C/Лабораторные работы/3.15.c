#include <stdio.h> 
#include <locale.h> 
#include <time.h> 

void main() 
{ 
		setlocale(0,""); 
			srand(time(NULL)); 
int n, i, *pm, sch=0, max_n=0; 
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
for (i=0; i<n; i++)
{
	if(*pm>0 && *pm%2==0)
	{
		sch++;
	}
	else
	{
    if(max_n<sch)
		max_n=sch;
		sch=0;
	}
	pm++;
}
printf ("\nРезультат: %d", max_n);
}

