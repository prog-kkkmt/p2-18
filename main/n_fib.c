#include "pch.h"

int fib(int N){
 if (N == 1 || N == 2)
    return 1; // первые 2 числа равны 1
  return fib(N - 1) + fib(N - 2);
}

void n_fib(){
    system("cls");
    system("cls");
    int N;
        printf("fib: ");
        scanf("%d", &N);
        for (int i = 1; i <= N; i++)
        printf("%d ", fib(i));
           system("pause");
}

