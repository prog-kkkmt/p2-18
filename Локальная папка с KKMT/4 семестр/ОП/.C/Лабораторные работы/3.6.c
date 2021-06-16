#include <stdio.h> 
#include <locale.h> 
#include <time.h> 

void main() 
{ 
	setlocale(0,""); 
		srand(time(NULL)); 
int n, j, x, i, *pm, *pm2, *pm3, max, max2; 
int mas[10], mas2[10], mas3[10]; 
		pm=&mas; 
		pm2=&mas2; 
		pm3=&mas3; 
			for (i=0; i<10; i++) 
				{ 
					*pm=rand()%100-50; 
					pm++; 
				} 
	pm-=10; 
			for (i=0; i<10; i++) 
				{ 
					*pm2=rand()%100-50; 
						pm2++; 
				} 
	pm2-=10; 
		printf ("Iao 1 iannea: "); 
			for (i=0; i<10; i++) 
				{ 
					printf ("%d ", *pm); 
					pm++; 
				} 
	pm-=10; 
		printf ("\nIao 2 iannea: "); 
			for (i=0; i<10; i++) 
				{ 
					printf ("%d ", *pm2); 
					pm2++; 
				} 
	pm2-=10; 
			for (i=0; i<10; i++) 
				{ 
					max=*pm; 
					if (*pm<*pm2) 
					*pm3=*pm2; 
			else 
					*pm3=*pm; 
						pm2++; 
					pm++; 
				pm3++; 
				} 
	pm3-=10; 
					printf ("\nIao 3 iannea: "); 
		for (i=0; i<10; i++) 
			{ 
				printf ("%d ", *pm3); 
				pm3++; 
			} 
}
