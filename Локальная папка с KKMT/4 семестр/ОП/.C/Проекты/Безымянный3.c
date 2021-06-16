#include <stdio.h>
#include <time.h>
int mas(int ii,int nn, int *a);
main ()
{
	int i,n,f;
	printf ("Vvedite col-vo elementov massiva: ");
	scanf ("%d",&n);
	int r[n];
	srand(time(NULL));
	printf ("Massiv: ");
	for (i=0;i<n;i++)
		printf("%3d ",r[i]=rand()%100-50);
	f=mas(0,n,r);
	printf ("\nColichestvo chetnih chisel: %d",f);	
}
int mas(int ii,int nn, int *a)
{
	if (ii==nn)
	return 0;
	else
	{
		if ((a[ii]%2)==0)
			return mas (ii+1,nn,a)+1;
		else
			return mas (ii+1,nn,a);
	}
}
