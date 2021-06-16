#include <stdio.h> 
#include <locale.h> 

void main () 
{ 
	setlocale(0,""); 
		int mas[10], i, j, x=0,*pm, so, ti, sch1=10, sch=0; 
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
				so=(*pm)*(*pm);
				sch1++;
				if(so == j)
			{
				sch=i;
				printf ("\nНайдено число: %d", *pm);
			pm++;
				printf ("\nНаш конечный массив: ");
		for (i=sch; i<10; i++)
			{
				ti=(*pm)*(*pm);
				printf ("%d ", ti); 
				pm++;
			}
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
