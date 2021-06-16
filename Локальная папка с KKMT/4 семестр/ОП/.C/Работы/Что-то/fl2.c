#include <stdio.h>
#include <conio.h>
#include <locale.h>
main()
{
    setlocale(0,"");
     int a[5];
      int b[5];
      int c[5];
      int i;
// определ€ем указатель на файл
     FILE *fout;
// открываем файл на запись
      //fou = fopen("C:\\Users\\user\\Desktop\\data.txt", "w");
        fout = fopen("f2.txt", "w");
// построчное записывание в файл
     printf("¬ведите массивы\n");
     for (i=0;i<5;i++)
     {
// ввод значений элементов массивов , нахождение суммы их запись в файл

         scanf("%d%d",&a[i],&b[i]);
         c[i]=a[i]+b[i];
         fprintf(fout,"%d %d %d\n",a[i],b[i],c[i]);
     }
// вывод массивов на экран
fclose(fout);
// открываем файл на чтение
fout = fopen("f2.txt", "r");
 for (i=0;i<5;i++)
     {fscanf(fout,"%d%d%d",&a[i],&b[i],&c[i]);
         printf("%d %d %d \n",a[i],b[i],c[i]);
     }
     getch();
// закрытие файла
     fclose(fout);
}
