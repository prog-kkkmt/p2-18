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
        printf("������� ������ : ");
        gets(s);
        for (i = 0; s[i] != '\0'; i++)
        { sym=s[strlen(s)-1-i];
        strncat(s1,&sym,1);
    //     strncat(s1,&s[strlen(s)-1-i],1); ����� �������� ������ 2-� ������� ����
        }
        printf("\n ����� ������\n");
        puts(s1);        // ����� �����
            if (strcmp(s1,s)==0) printf("������ �����, ����� �������� ����� ������� � ��������.");
                else   printf("������  �� �����");
}
