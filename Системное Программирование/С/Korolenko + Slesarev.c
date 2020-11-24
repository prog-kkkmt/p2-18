#include <stdio.h>
#include <locale.h>
#include <time.h>

//даны три числа найти наименьшее 12

void main(){
    setlocale(0,"");
    int i,j,min_value,n;
        printf("¬ведите кол-во:\n");
        scanf ("%d", &n);
        int mas[n];
        printf("¬ведите 3 числа:\n");
            for (i = 0; i < n; i++) {
                scanf ("%d", &mas[i]); }
            for(i = 0; i < n; i++)
                if(mas[i] < min_value) min_value = mas[i];
                printf("%i", min_value);
}
