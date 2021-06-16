#include <stdio.h>
#include <conio.h>
main()
{     int a[10];
      int b[10];
      int c[10];
      int i;
// определяем указатель на файл
     FILE *fin;
// открываем файл на чтение
      //fin = fopen("C:\\Users\\user\\Desktop\\data.txt", "r");
        fin = fopen("f1.txt", "r");
// построчное считывание из файла
     for (i=0;i<10;i++)
     {
// считывание строки из  трех значений файла и запись в массивы
         fscanf(fin,"%d%d%d",&a[i],&b[i],&c[i]);
     }
// вывод массивов на экран
 for (i=0;i<10;i++)
     {
         printf("%d %d %d \n",a[i],b[i],c[i]);
     }
     getch();
// закрытие файла
     fclose(fin);
}
