#include <stdlib.h>
#include <Windows.h>
#include <stdio.h>
#include <string.h>
int main(void)
{
    SetConsoleCP (1251);
    SetConsoleOutputCP (1251);

    char s[80], sym;
    int poz=-1, i;
    printf("������� ������ : ");
    gets(s);
        sym = '.';
  for (i = 0; s[i] != '\0'; i++)
    {
    if (s[i] ==sym)     {poz=i; break;}
    }
    if (poz!=-1)
        {printf("� ������\n");
            puts(s);      // ����� ������
        printf("������ ");
    putchar(sym); // ����� �������
        printf(" ����� ������� %d ",poz+1);}
    else printf("��� ����� � ������");
}
