#include <stdio.h>
#include <stdlib.h>

int main()
{
	int n;
	printf ("Vvedite col-vo elementov: ");
	scanf ("%d",&n);
	int *pa=(int *)malloc(sizeof (int)*n);
	for (int i=0;i<n;i++){
		printf ("Vvedite %d elemnt:\t",i+1);
		scanf("%d",pa+i);
	}
	for (int i=0;i<n-1;i++)
	{
		for (int j=(n-1);j>i;j--)
		{
			if (*(pa+j-1)>*(pa+j))
			{
				int t = *(pa+j-1);
				*(pa+j-1)=*(pa+j);
				*(pa+j)=t;
			}
		}
	}
	for (int i=0;i<n;i++)
		printf ("%d\t",*(pa+i));
	free (pa);
	return 0;
}