#include<stdio.h>
int main()
{
    int a[100][100];
    int m,n;

    printf("m-");
    scanf("%i",&m);
    printf("n-");
    scanf("%i",&n);

    int i,j;
    for (i=0; i<m; i++){

        for (j=0; j<n; j++){

            scanf("%i", &a[i][j]);
        }
    }
    for (i=0; i<m; i++){
        for (j=0; j<n; j++){
            printf("   %i ",a[i][j]);
        }
        printf("\n");
    }
    return 0;
}
