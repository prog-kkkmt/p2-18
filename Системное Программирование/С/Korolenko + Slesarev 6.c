#include <stdio.h>
#include <locale.h>
#include <time.h>
Дан массив A размер N
Вывести его элементы с чётными номерами в порядке возрастания номеров
А2 а4 а6
условный оператор


void main(){
    setlocale(0,"");
        int i,n;
        scanf("%d",&n);
        int mas[n];
            for ( i = 0; i < n; i ++){
                mas[i] = rand ()%10; //рандомные числа
                printf("%d ",mas[i]);
            }
                printf("\n");
            i=1;
            while(i<=n){
                printf("%d ",mas[i]);
                i=i+2;
            }
    }
