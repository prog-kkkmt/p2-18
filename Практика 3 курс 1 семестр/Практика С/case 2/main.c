/*Case1. ���� ����� ����� � ��������� 1�7.
������� ������ � �������� ��� ������, ��������������� ������� �����
(1 � ������������, 2 � �������� � �. �.).*/

#include <stdio.h>

int main()
{
   int a;
   scanf("%d", &a);
   switch(a){
   case 1:
        printf("Ploho");
        break;
    case 2:
        printf("Neudovletvoritelno");
        break;
    case 3:
        printf("Udovletvoritelno");
        break;
    case 4:
        printf("Horosho");
        break;
    case 5:
        printf("Otlichno");
        break;
    default:
        printf("Oshibka");
        break;

   }
   return 0;
}
