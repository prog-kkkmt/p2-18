#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include <locale.h>

int main()
{
    setlocale(0,"");
    int n, i, max=0, *pm, pos,*tmp, k;
    char flag = 1;
    printf("Введите n ");
    scanf("%d", &n);
    int mas[n];
    int *mas_sort[n];
    pm = &mas;
    for(i=0;i<n;i++)
    {
        scanf("%d", pm);
        pm++;
    }
    pm -=n;
    for(i=0;i<n;i++)
    {
        printf("%d ", *pm);
        pm++;
    }
    pm-=n;
    for (i=0;i<n;i++)
    {
    if (max< *pm)
    {
     max = *pm;
     pos = i;
    }
    pm++;
    }
    pm-=n;
    printf("\n Максимальное число массива: %d \n Его позиция: %d", max, pos);
    // Сортировка
    for(i=0;i<n;i++)
    {
     mas_sort[i] = &mas[i];
    }
    k = pos;
do{
    flag = 0;
    for(i=k+1;i<n;i++)
    {
        if(*mas_sort[i]>*mas_sort[i-1])
        {
            tmp = mas_sort[i];
            mas_sort[i] = mas_sort[i-1];
            mas_sort[i-1] = tmp;
            flag = 1;
        }
    }
}while(flag);
printf("\n");
 for(i=0;i<n;i++)
    {
        printf("%d ", *mas_sort[i]);
            }
}
