#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <locale.h>
int main() {
    setlocale(0,"");
  char s[80], sym;
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
  int l=strlen(s);
  float p= count*100.0/l;
  printf("� ������\n");
  puts(s);      // ����� ������
  printf("������ ");
  putchar(sym); // ����� �������
  printf(" ����������� %d ���, ������� ��������� ������� = %f %%", count,p);
}

