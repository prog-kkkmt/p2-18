#include <stdlib.h>
#include <Windows.h>
#include <stdio.h>
#include <string.h>
int main(void)
{
    SetConsoleCP (1251);
    SetConsoleOutputCP (1251);

    int i,pr=0;
        char str[12],Marx[4][12]={"�������","�����","������","�������"};
    printf("��������� ���������� �� ����� ����\n������� ������ ��������� -> ");
        scanf("%s",&str);
    for(i=0;i<4 && pr!=1;i++)
        if (!strcmp(Marx[i],str)) {printf("%d", i+2);pr=1;}
            if (pr!=1) printf("��� ����� ������!");
return 0;
}
