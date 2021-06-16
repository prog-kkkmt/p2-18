
#include <stdio.h>
#include <stdlib.h>


int **array(int ROW, int COL)
    {
    int i,**p= NULL;
    p = (int**) malloc(ROW * sizeof(int*));
    for (i = 0; i < ROW; i++)
    p[i] = (int*) malloc(COL * sizeof(int));
    return p;
    }
void array_destroyer(int **p,  int ROW)
    {
    int i;
    for ( i = 0; i < ROW ; i++)
              free(p[i]);
    free(p);
     }

void main()
{
    int **matrix,i,j,m,n;
    // создание массива
    printf("m,n=?");
    scanf("%d%d",&m,&n);
    matrix = array(m, n);

        for ( i = 0; i < m; i++)
            {
        for ( j = 0; j < n; j++) {
            matrix[i][j] = rand()%100-50;
                printf("%d\t",matrix[i][j] ) ;
                                  }
                                    printf("\n");
             }
array_destroyer(matrix, m);
}



