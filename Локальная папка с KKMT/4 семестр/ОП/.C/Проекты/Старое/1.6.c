#include <stdlib.h>
#include <Windows.h>
#include <stdio.h>
#include <string.h>
int main(void)
{
    SetConsoleCP (1251);
    SetConsoleOutputCP (1251);
  char s[88], sym;
  int count, i;

  printf("������� ������ : ");
  gets(s);
  printf("������� ������ : ");
  sym = getchar();
  count = 0;
  for (i = 0; s[i] != '\0'; i++)
  {
    if (s[i] == sym)
      count++;
  }
  printf("� ������\n");
  puts(s);      // ����� ������
  printf("������ ");
  putchar(sym); // ����� �������
  printf(" ����������� %d ���", count);
  getchar();
  return 0;
}
