#include <stdio.h> 
#include <locale.h> 
#include <time.h>

void main() 
{ 
	setlocale(0,"");
		srand(time(NULL));
int a, j, x, i, *pm, *pm2, *pm3;
				printf ("������� ������ ������� 1 � 2\n");
			scanf ("%d%d", &a,&j);
		x=a+j;
int mas[a], mas2[j], mas3[x];
		pm=&mas;
		pm2=&mas2;
		pm3=&mas3;
	for (i=0; i<a; i++) 
		{
			*pm=rand()%100-50;
				pm++; 
		}
	pm-=a;
		for (i=0; i<j; i++) 
			{
				*pm2=rand()%100-50;
				pm2++; 
			}
	pm2-=j;
				printf ("��� 1 ������: "); 
		for (i=0; i<a; i++) 
			{
				printf ("%d ", *pm); 
					pm++; 
			}
	pm-=a;
				printf ("\n��� 2 ������: "); 
			for (i=0; i<j; i++) 
				{
					printf ("%d ", *pm2); 
						pm2++; 
				}
	pm2-=j;
					for (i=0; i<a; i++)
						{
							*pm3=*pm;
							pm3++;
							pm++;
						}
							for (i=a; i<x; i++)
								{
									*pm3=*pm2;
									pm3++;
									pm2++;
								}
	pm3-=x;
					printf ("\n��� 3 ������: "); 
		for (i=0; i<x; i++) 
			{
				printf ("%d ", *pm3); 
				pm3++; 
			}
}
