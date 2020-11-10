#include "pch.h"

void sort_viborom(){
    int n;
    system("cls");
    printf("¬ведите N: ");
    scanf("%d", &n);
        int* mass;
        mass = (int *)malloc(n * sizeof(int));
        for (int i = 0; i < n; i++){
            mass[i] = rand() % 50 - 8;
            printf("%d ", mass[i]);
        }
    int min, temp;
    for (int i = 0; i < n - 1; i++){
        min = i;

        for (int j = i + 1; j < n; j++){
            if (mass[j] < mass[min])
            min = j;
        }
            temp = mass[i];
            mass[i] = mass[min];
            mass[min] = temp;
  }
  printf("\n");
   for (int i = 0; i < n; i++){
            printf("%d ", mass[i]);
        }
    free(mass);
    system("pause");
}

