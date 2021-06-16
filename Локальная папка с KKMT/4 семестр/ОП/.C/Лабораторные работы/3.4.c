#include <stdio.h> 
#include <locale.h> 

void main() 
{ 
setlocale(0,""); 
		int a[10], i, j, x=0, *pm;
			pm=&a;
				printf ("Введите элементы: "); 
	for (i=0; i<10; i++) 
		{ 
			scanf ("%d", pm); 
			pm++; 
		} 
					pm-=10; 
				printf ("\nНаш массив: "); 
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
					printf ("\nРезультат %d", x);
				return 0;
			}	
					pm++;
		}
	printf ("\nРезультат %d", x);
}


