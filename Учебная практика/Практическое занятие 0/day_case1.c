/*Case1. ���� ����� ����� � ��������� 1�7. ������� ������ � �������� ��� ������,
��������������� ������� ����� (1 � ������������, 2 � �������� � �. �.).*/
#include <locale.h>
#include <stdio.h>
int main(){
    int day;
    scanf ("%d", & day);
    setlocale (LC_ALL, "rus");
    switch (day){
    case 1:
        printf ("�����������");
        break;
    case 2:
        printf ("�������");
        break;
    case 3:
        printf ("�����");
        break;
    case 4:
        printf ("�������");
        break;
    case 5:
        printf ("�������");
        break;
    case 6:
        printf ("�������");
        break;
    case 7:
        printf ("�����������");
        break;
    }
    return 0;
}
