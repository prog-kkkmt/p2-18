#include <stdlib.h>
#include <Windows.h>
#include <stdio.h>
#include <string.h>
int main(void)
{
    SetConsoleCP (1251);
    SetConsoleOutputCP (1251);
char s[255];
printf("¬ведите текст: ");
gets(s);
puts(s);
}
