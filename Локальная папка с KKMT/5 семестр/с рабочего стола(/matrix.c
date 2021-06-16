#include <stdio.h>

int main(void)
{
    int a[10][10];
    int m,n;

    printf("M: ");
    scanf("%i",&m);
    printf("N: ");
    scanf("%i",&n);

    int i,j;
    for (i=0; i<m; ++i){
        printf("%i : \n", i+1);
        for (j=0; j<n; ++j){
            printf("%i ", j+1);
            scanf("%i", &a[i][j]);
        }
    }


    for (i=0; i<m; ++i){
        for (j=0; j<n; ++j){
            if (j%2==0){
                printf("%i ",a[i][j]);
            } else {
                printf("%i ",a[n-i-1][j]);
            }
        }
        printf("\n");
    }
    return 0;
}
