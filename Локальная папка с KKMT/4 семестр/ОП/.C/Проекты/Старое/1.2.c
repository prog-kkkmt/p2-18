#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Windows.h>
main()
{
    SetConsoleCP (1251);
    SetConsoleOutputCP (1251);
    char m1[80] = "First string";
    char m2[80] = "Second String";

    char m3[80];
    puts (m1);
    puts(m2);
    strncpy(m3, m1, 6);  // не добавляет '\0' в конце строки
    puts("Result strncpy(m3, m1, 6)");
    puts(m3);
    strcpy(m3, m1);
    puts("Result strcpy(m3, m1)");
    puts(m3);
    puts("Result  strcmp(m3, m1) =  ");
    printf("%d\n", strcmp(m3, m1));
    strncat(m3, m2, 5);
    puts("Result  strncat(m3, m2, 5)");
    puts(m3);
    strcat(m3, m2);
    puts(" Result  strcat(m3, m2)");
    puts(m3);
    puts("Result   strlen(m1) : ");
    printf("%d\n", strlen(m1));
    strnset(m3, 'f', 7);
    puts("Result strnset(m3, 'f', 7)");
    puts(m3);
    strset(m3, 'k');
    puts("Result strnset(m3, 'k')");
    puts(m3);
    getchar();
    return 0;}
