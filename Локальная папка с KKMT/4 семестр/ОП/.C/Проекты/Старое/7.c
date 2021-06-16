#include <stdlib.h>
#include <Windows.h>
#include <stdio.h>
#include <string.h>
int main(void)
{
    SetConsoleCP (1251);
    SetConsoleOutputCP (1251);

    char s[80]="",s1[80],s2[80],sym;
int  i;
printf("Введите 1 слово : ");
    gets(s1);
printf("Введите 2 слово : ");
    gets(s2);
for (i = 0; s1[i] != '\0'; i++)
    { sym=s1[strlen(s1)-1-i];
            strncat(s,&sym,1);
        //     strncat(s1,&s[strlen(s)-1-i],1); Можно напрямую вместо 2-х строчек выше
    }
    printf("  Обратное слово первому\n   ");
        puts(s);        // Вывод обратное слово первому
    if (strcmp(s2,s)==0) printf("Слова обратны между собой");
        else   printf("Слова не обратны между собой ");
}
