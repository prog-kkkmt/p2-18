#define N 10
#include "pch.h"

void sort_bubble(){
    system("cls");
    int mass[N];
    srand(time(NULL));
        for (int i = 0; i < N; i++){
            mass[i] = rand() % 50 - 8;
            printf("%d ", mass[i]);
        }
        for(int i = 0 ; i < N - 1; i++){
            for(int j = 0 ; j < N - i - 1 ; j++){
               if(mass[j] > mass[j+1]) {
                  int tmp = mass[j];
                  mass[j] = mass[j+1] ;
                  mass[j+1] = tmp;
               }
            }
        }
        printf("\n");
        for (int i = 0; i < N; i++){
            printf("%d ", mass[i]);
        }
        printf("\n");
        system("pause");
}
