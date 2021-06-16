#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
main()
{
// задаем строковые перменные
char st[100];

//определяем указатель на файл
      FILE *fin;
// настриваем работу с Кириллицей
      setlocale(0, "");
// открываем файл на чтение
      fin = fopen("f6.txt", "r");
          if (fin == NULL) {
        printf("Error opening file");
        getch();
                                    }
// считываем первую строку из файла
while (!feof(fin))
        {if ( NULL != fgets ( st, 100, fin ) )

        // выводим строку на экран
        printf("%s \n",st);}

   fclose(fin);
}
