#include <stdlib.h>
#include <Windows.h>
#include <stdio.h>
#include <string.h>
int main(void)
{
    SetConsoleCP (1251);
    SetConsoleOutputCP (1251);
int i;
    char Marx[4][12]={"�������","�����","������","�������"};
    printf("��������� ���������� �� ����� ����\n ������� ����� ����� -> ");
    scanf("%d",&i);
        if (i<2 || i>5)
    printf("��� ����� ������!");
  else
    printf(Marx[i-2]);
return 0;
}
