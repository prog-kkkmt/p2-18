/*Case2�. ���� ����� ����� K. ������� ������-�������� ������, ��������������� ����� K
(1 � ������, 2 � ��������������������, 3 � ������������������, 4 � �������, 5 � ��������).
 ���� K �� ����� � ��������� 1�5, �� ������� ������ �������.*/

#include <stdio.h>

int main()
{
   int a;
   scanf("%d", &a);
   switch(a){
   case 1:
        printf("Ponedelnik");
        break;
    case 2:
        printf("Vtornik");
        break;
    case 3:
        printf("Sreda");
        break;
    case 4:
        printf("Cgetverg");
        break;
    case 5:
        printf("Pyatnica");
        break;
    case 6:
        printf("Subbota");
        break;
    case 7:
        printf("Voskresenie");
        break;
    default:
        printf("Nepravilno ukazan den");
        break;
}
return 0;
}
