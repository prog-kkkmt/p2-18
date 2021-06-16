#define N 10
#include "pch.h"

void find_in_list2(){
    system("cls");
    int mass[N];
    int s, a=0;
    srand(time(NULL));
        for (int i = 0; i < N; i++){
            mass[i] = rand() % 50 - 8;
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
        for (int i = 0; i < N; i++){
            printf("%d ", mass[i]);
        }
        printf("\n");
        scanf("%d", &s);
            for (int i = 0; i < N; i++){
                if(mass[i] == s){
                    printf("Номер позиции: %d\n", i+1);
                    a++;
                }
            }
        if(a==0){
            printf("Нет такой позиции!");
        }

        printf("\n");
        system("pause");
}
