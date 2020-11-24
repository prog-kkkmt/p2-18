#include "pch.h"

void sort_input(){
    int n;
    printf("¬ведите N: ");
    scanf("%d", &n);
    int* mass;
    mass = (int *)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
       mass[i] = rand() % 50 - 8;

    int Element, loc;
        for (int i = 1; i < n; i++){
            Element = mass[i];
            loc = i - 1;

            while(loc >= 0 && mass[loc] > Element){
                mass[loc + 1] = mass[loc];
                loc = loc - 1;
            }
            mass[loc+1] = Element;
        }
    for (int i = 0; i < n; i++)
        printf("%d ", mass[i]);
        printf("\n");
    free(mass);
    system("pause");
}
