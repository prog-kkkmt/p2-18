#include <stdio.h> 
#include <locale.h> 

void main () 
{ 
	setlocale(0,""); 
		int mas[10], i, j, x=0,*pm, so, ti, sch1=10, sch=0; 
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
				so=(*pm)*(*pm);
				sch1++;
				if(so == j)
			{
				sch=i;
				printf ("\n������� �����: %d", *pm);
			pm++;
				printf ("\n��� �������� ������: ");
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
				printf ("\n��� �������� ������: ");
		for (i=0; i<10; i++) 
			{
				printf ("%d ", *pm);
				pm++;
			}
}
