#include <stdio.h>
#include <locale.h>
#include <time.h>

Дано целое число N (>1) Вывести наибольшее из целых чисел К
Для которых суммма 1+2+,,,+К будет меньше или равна N и саму эту сумму

void main(){
    setlocale(0,"");

    int k=0,n,sum=0,i;
    scanf("%d",&n);
        while(sum <= n){
            k++;
            sum+=k;
        }
        printf("K=%d Summ=%d",k-1,sum-k);
    }
