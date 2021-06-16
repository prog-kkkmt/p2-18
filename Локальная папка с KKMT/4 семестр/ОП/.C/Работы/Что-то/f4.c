#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
main()
{
// задаем строковые перменные
char st1[100];
char st2[100];
//определяем указатель на файл
      FILE *fin;
// настриваем работу с Кириллицей
      setlocale(0, "");
// открываем файл на чтение
      fin = fopen("f5.txt", "r");
          if (fin == NULL) {
        printf("Error opening file");
        getch();
                                    }
// считываем первую строку из файла
if ( NULL != fgets ( st1, 100, fin ) )
{
// выводим строку на экран
printf("%s \n",st1);}
// считываем вторую строку из файла
if ( NULL != fgets ( st2, 100, fin ) )
{
// выводим строку на экран
printf("%s \n",st2);}
// закрываем файл на чтение
   fclose(fin);
}
