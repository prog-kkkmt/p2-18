#include <stdio.h>
#include <stdlib.h>
int main()
{
    int n, i;
    scanf("%d", &n);
    int *pa=(int*)malloc(sizeof(int)*n);
    for(i=0;i<n;i++)
    {
        scanf("%d", pa+i);
    }
    printf("max: %d, min: %d", *(pa+i-1), *pa);
    free(pa);
    return 0;
}
