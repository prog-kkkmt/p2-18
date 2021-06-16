  #include <stdlib.h>
#include <Windows.h>
#include <stdio.h>
#include <string.h>
int main(void)
{
    SetConsoleCP (1251);
    SetConsoleOutputCP (1251);

      char s[80],s1[80]="",sym;
        int  i;
        printf("Введите строку : ");
        gets(s);
        for (i = 0; s[i] != '\0'; i++)
        { sym=s[strlen(s)-1-i];
        strncat(s1,&sym,1);
    //     strncat(s1,&s[strlen(s)-1-i],1); Можно напрямую вместо 2-х строчек выше
        }
        printf("\n Новая строка\n");
        puts(s1);        // Вывод слова
            if (strcmp(s1,s)==0) printf("Строки равны, слово читается слева направо и наоборот.");
                else   printf("Строки  не равны");
}
