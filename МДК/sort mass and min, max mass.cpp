#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void sort(int *A, int N)
{
	int t;
	for(int i = 0; i < N-1; i++)
	{
	    for(int j = 0; j < N-1; j++)
            if(*(A+j) > *(A+j+1))
            {
                t = *(A+j);
                *(A+j) = *(A+j+1);
                *(A+j+1) = t;
            }
	}
}

int main()
{
	srand(time(0));
	int n;
	scanf("%d", &n);
	int *pa = (int*)malloc(sizeof(int) * n);
	for(int i = 0; i < n; i++)
	{
		*(pa+i) = rand()%10-5;
		printf("%d ", *(pa+i));
	}

	sort(pa, n);
printf("\n\n");
	for(int i = 0; i < n; i++)
	{
		printf("%d ", *(pa+i));
	}

	printf("\n\nmin: %d max: %d", *pa, *(pa+n-1));

	free(pa);

	return 0;
}
