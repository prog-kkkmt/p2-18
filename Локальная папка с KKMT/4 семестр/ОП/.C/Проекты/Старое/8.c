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
          printf("������� ������ : ");
          gets(s);
          printf("������� ������ : ");
          sym = '+';
          count = 0;
          for (i = 0; s[i] != '\0'; i++)
          {
            if (s[i] == sym)
              count++;
          }
          if(count==0 )
          {printf("� ������\n");
          puts(s);      // ����� ������
          printf("������ ");
          putchar(sym); // ����� �������
          printf(" �� ����������� ");}
          else  printf("\n ������ '+' � ������  ����������� %d ��� ",count);
  return 0;
}

