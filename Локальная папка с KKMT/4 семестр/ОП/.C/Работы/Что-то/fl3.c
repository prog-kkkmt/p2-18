#include <stdio.h>
#include <conio.h>
#include <locale.h>
#include <string.h>
main()
{
    setlocale(0,"");
     int a[5];
      int b[5];
      int c[5];
      int i;
      char str[20];
// определ€ем указатель на файл
     FILE *fout;
// открываем файл на запись
      //fou = fopen("C:\\Users\\user\\Desktop\\data.txt", "w");
        fout = fopen("f4.txt", "w");
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
// переоткрываем файл на чтение
 freopen("f4.txt", "r",fout);
 for (i=0;i<5;i++)
     {fscanf(fout,"%d%d%d",&a[i],&b[i],&c[i]);
         printf("%d %d %d \n",a[i],b[i],c[i]);
     }
freopen("f4.txt", "a",fout);
printf("введите строку");
scanf("%s",str);
fprintf(fout,"%s",str);
     getch();
// закрытие файла
     fclose(fout);
}
