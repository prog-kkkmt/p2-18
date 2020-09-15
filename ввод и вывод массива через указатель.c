#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <time.h>
int main()
{
    srand(time(NULL));
    setlocale(0,"");
    int n;
    printf("¬ведите количество элементов в массиве: ");
    scanf("%d", &n);
    int *pa = (int *)malloc(sizeof(int)*n);
    printf("\n—генерированный массив:\n");
    for (int i = 0; i < n; i++)
    {
        *(pa+i)=rand()%10;
        printf("%d ", *(pa+i));
    }
    for (int i = 0; i < n-1; i++)
	{
		for (int j = (n-1); j>i; j--)
		{
			if (*(pa+j-1) > *(pa+j))
			{
				int t = *(pa+j-1);
				*(pa+j-1) = *(pa+j);
				*(pa+j) = t;
			}
		}
	}
	printf ("\n\nќтсортированный массив:\n");
	for (int i=0; i<n; i++)
		printf ("%d ", *(pa+i));
    free (pa);
    return 0;
}
