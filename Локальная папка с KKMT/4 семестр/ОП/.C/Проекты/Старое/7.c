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
printf("������� 1 ����� : ");
    gets(s1);
printf("������� 2 ����� : ");
    gets(s2);
for (i = 0; s1[i] != '\0'; i++)
    { sym=s1[strlen(s1)-1-i];
            strncat(s,&sym,1);
        //     strncat(s1,&s[strlen(s)-1-i],1); ����� �������� ������ 2-� ������� ����
    }
    printf("  �������� ����� �������\n   ");
        puts(s);        // ����� �������� ����� �������
    if (strcmp(s2,s)==0) printf("����� ������� ����� �����");
        else   printf("����� �� ������� ����� ����� ");
}
