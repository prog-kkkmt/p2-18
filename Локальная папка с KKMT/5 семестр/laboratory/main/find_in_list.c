#define N 10
#include "pch.h"

void find_in_list(){
    system("cls");
    int mass[N];
    int s, a=0;
    srand(time(NULL));
    //��������� ����
        for (int i = 0; i < N; i++){
            mass[i] = rand() % 50 - 10;
            printf("%d ", mass[i]);
        }
        printf("\n");
        scanf("%d", &s);
        for (int i = 0; i < N; i++){
            if(mass[i] == s){
                printf("����� �������: %d\n", i+1);
                a++;
            }
        }
        if(a==0){
            printf("��� ����� �������!");
        }
        printf("\n");
        system("pause");
}
