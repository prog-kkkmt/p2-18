#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main (){
    srand(time(0));
int n;
scanf("%d", &n);
int *pa=(int *)malloc (sizeof(int)*n);
for (int i=0; i<n;++i)
    *(pa+i) = rand()%10;
for (int i=0; i<n;++i)
    printf("%d", *(pa+i));
free(pa);
return 0;
}
