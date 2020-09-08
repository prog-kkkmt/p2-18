//Даны целые положительные числа M и N. Сформировать целочисленную матрицу размера M × N,
//у которой все элементы I-й строки имеют значение 10·I (I = 1, …, M).

#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>

int main()
{
    int *a;
    int m, n;

    printf("enter m \n");
    scanf("%d", &m);

    printf("enter n \n");
    scanf("%d", &n);

    a = (int*)malloc(n * m * sizeof(int));

    for(int i = 0; i < m; ++i){
        for(int j = 0; j < n; ++j){
            a = (i * 10);
            a++;
        }
    }
    a = a - m - n;

    for(int i = 0; i < m; ++i){
        for(int j = 0; j < n; ++j){
            printf("%d ", a + i * m + j);
            a++;
        }
        printf("\n");
    }


    return 0;
}
