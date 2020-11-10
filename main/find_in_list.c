#define N 10
#include "pch.h"

void find_in_list(){
    system("cls");
    int mass[N];
    int s, a=0;
    srand(time(NULL));
    //рандомный ввод
        for (int i = 0; i < N; i++){
            mass[i] = rand() % 50 - 10;
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
