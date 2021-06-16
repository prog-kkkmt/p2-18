#include <stdio.h> 
#include <locale.h> 
#include <time.h> 
#include <math.h>
void main() 
{ 
		setlocale(0,""); 
	srand(time(NULL)); 
int n, i, *pm, sum_NP=0, kol_OCH=0, mest; 
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
				if (i%5==0)
				*pm=powf(*pm, 5);
		   	pm++;
			}
	pm-=n;
			printf ("\nНаш итоговый массив: "); 
		for (i=0; i<n; i++) 
			{ 
				printf ("%d ", *pm); 
				pm++; 
			} 
	pm-=n;
}

