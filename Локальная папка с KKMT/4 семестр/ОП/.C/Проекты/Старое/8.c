#include <stdlib.h>
#include <Windows.h>
#include <stdio.h>
#include <string.h>
int main(void)
{
    SetConsoleCP (1251);
    SetConsoleOutputCP (1251);
        char s[80], sym;
          int count, i;
          printf("Введите строку : ");
          gets(s);
          printf("Введите символ : ");
          sym = '+';
          count = 0;
          for (i = 0; s[i] != '\0'; i++)
          {
            if (s[i] == sym)
              count++;
          }
          if(count==0 )
          {printf("В строке\n");
          puts(s);      // Вывод строки
          printf("символ ");
          putchar(sym); // Вывод символа
          printf(" не встречается ");}
          else  printf("\n символ '+' в строке  встречается %d раз ",count);
  return 0;
}

