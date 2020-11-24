#include <stdio.h>
#include <locale.h>
#include <time.h>

ƒано целое число N и набор из N чисел
Ќайти ћинимальное положение число из данного набора
≈сли положительное число    в наборе отсутсвует то вывести 0


void main(){
    setlocale(0,"");
    int i,n,m;
        scanf("%d",&n);
            int mas[n];
        for ( i = 0; i < n; i ++){
            mas[i] = rand ()%10-10; //рандомные числа
                printf("%d ",mas[i]);
        }
        m=mas[0];
        for ( i = 0; i < n; i ++){
            if(mas[i]>m)
                m=mas[i];
        }
            if(m>0){
                printf("\n%d",m);
            }
            else printf("\n0,00");
    }
