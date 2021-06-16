#include<stdio.h>
#include<conio.h>
#include<locale.h>
#include<stdlib.h>
#include<time.h>
main()
{
setlocale(0,"");
srand (time(NULL));
int m,n,i,j;;
printf("m=?, n=?\n");
scanf("%d%d",&m,&n);
int ar[m][n],sumstl[n],sumstr[m];
    // ввод вывод массива
    for (i=0;i<m;i++)
            {       for(j=0;j<n;j++)
            {ar[i][j]=rand()%100-50;
            printf("%5d",ar[i][j]);}
     printf("\n");
     }

  // Создание  одномерного массива из сумм элементов столбца
          for(j=0;j<n;j++)
         {sumstl[j]=0;
           for(i=0;i<m;i++)
           sumstl[j]+=ar[i][j];
         }

// вывод массива
printf("\n Массив из сумм элементов столбцов");
for(j=0;j<n;j++)
printf("%5d",sumstl[j]);
            //нахождение минимума среди сумм столбцов
            int min=sumstl[0],nmin=0;
            for(j=0;j<n;j++)
            if (sumstl[j]<min) {min=sumstl[j];nmin=j;}
            printf("\n min=%5d, номер=%5d",min,nmin);
// замена столбца матрицы с наименьшей суммой нулями
 for(i=0;i<m;i++)
    ar[i][nmin]=0;
                 // вывод получившегося массива
                 printf("\n Изменившийся массив:");
                  printf("\n");
                 for (i=0;i<m;i++)
                    {       for(j=0;j<n;j++)
                             printf("%5d",ar[i][j]);
                     printf("\n");
                     }


// Создание  одномерного массива из сумм элементов строки
for(i=0;i<m;i++)
 {sumstr[i]=0;
   for(j=0;j<n;j++)
   sumstr[i]+=ar[i][j];
 }
// Вывод массива сумм строк
              printf("\n Массив из сумм элементов строк");
              for(i=0;i<m;i++)
              printf("%5d",sumstr[i]);
              int max=sumstr[0],nmax=0;
                        for(i=0;i<m;i++)
                        if (sumstr[i]>max) {max=sumstr[i];nmax=i;}
                        printf("\n max=%5d, номер=%5d",max,nmax);
// замена строки матрицы с наибольшей суммой строк на элементы увеличенные в 3 раза
 for(j=0;j<n;j++)
    ar[nmax][j]*=3;
// вывод получившегося массива
             printf("\n Изменившийся массив:");
              printf("\n");
                          // ввод вывод массива
                         for (i=0;i<m;i++)
                            {       for(j=0;j<n;j++)
                                     printf("%5d",ar[i][j]);
                             printf("\n");
                             }


return 0;
}
