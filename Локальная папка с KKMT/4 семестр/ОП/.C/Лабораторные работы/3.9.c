#include <stdio.h> 
#include <locale.h> 
#include <time.h> 

void main() 
{ 
	setlocale(0,""); 
		srand(time(NULL)); 
int n, i, *pm, sum_NP=0, kol_OCH=0, mest; 
			printf ("������� ������ �������: "); 
		scanf ("%d", &n);
int mas[n];
	pm=&mas;
		for (i=0; i<n; i++)
		{
			*pm=rand()%100-50;
			pm++;
		}
	pm-=n;
			printf ("��� ������: "); 
		for (i=0; i<n; i++) 
			{ 
				printf ("%d ", *pm); 
				pm++; 
			} 
	pm-=n;
		for (i=0; i<n; i++)
			{
				if (i%2==0 && *pm<0)
				kol_OCH++;
				if (i%2!=0 && *pm>0)
				sum_NP+=*pm;
				pm++;
			}
		printf ("\n����� �����. ���������: %d", sum_NP);
	printf ("\n����������� �����. ���������: %d", kol_OCH);
}

