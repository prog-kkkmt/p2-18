#include <stdio.h> 
#include <locale.h> 
#include <time.h> 

void main() 
{ 
		setlocale(0,""); 
	srand(time(NULL)); 
int n, j, x, i, *pm, *pm2, *pm3, tmp, flag, min, mest=0; 
			printf ("Введите размер массива 1 и 2\n"); 
		scanf ("%d%d", &n,&j); 
	x=n+j; 
int mas[n], mas2[j], mas3[x], *p[x]; 
		pm=&mas; 
		pm2=&mas2; 
		pm3=&mas3; 
for (i=0; i<n; i++) 
	{ 
		*pm=rand()%100-50; 
		pm++; 
	} 
pm-=n; 
for (i=0; i<j; i++) 
	{ 
		*pm2=rand()%100-50; 
		pm2++; 
	} 
pm2-=j; 
printf ("Наш 1 массив: "); 
for (i=0; i<n; i++) 
	{ 
		printf ("%d ", *pm); 
		pm++; 
	} 
pm-=n; 
printf ("\nНаш 2 массив: "); 
for (i=0; i<j; i++) 
	{ 
		printf ("%d ", *pm2); 
		pm2++; 
	} 
pm2-=j; 
for (i=0; i<n; i++) 
	{ 
		*pm3=*pm; 
		pm++; 
		pm3++; 
	} 
for (i=n; i<x; i++) 
	{ 
		*pm3=*pm2; 
		pm2++; 
		pm3++; 
	} 
pm3-=x; 
printf ("\nНаш 3 массив: "); 
for (i=0; i<x; i++) 
	{
		printf ("%d ", *pm3); 
		pm3++; 
	}
pm3-=x;
min=*pm;
for (i=0; i<(x-1); i++)
	{
		if (min>*(pm3+1))
		{
			min=*(pm3+1);
			mest=i+1;
    	}
    pm3++;
	}
printf ("\nНаш мин элемент и его место: %d %d", min, mest);
for (i=0; i<x; i++) 
	{ 
		p[i]=&mas3[i];
	} 
do { 
	flag=0;
	for (i=1; i<mest+1; i++) 
	{ 
		if (*p[i]>*p[i-1])
		{ 
			tmp=p[i];
			p[i]=p[i-1];
			p[i-1]=tmp;
			flag=1;
		} 
	} 
	} 
while (flag); 
printf ("\nНаш отсортированный 3 массив: "); 
for (i=0; i<mest; i++) 
	{ 
		printf ("%d ", *p[i]);
	} 
}
