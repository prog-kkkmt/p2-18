#include <stdio.h>
#include <locale.h>
#include <time.h>

ƒан набор нулевых целых чисел
признак его завершщени€ 0
вывести кол-во чисел в наборе

void main(){
    setlocale(0,"");
        int n=100,sum=-1;

    while (n!=0){
        scanf("%d",&n);
        sum++;
    }
    printf("%d",sum);
}
