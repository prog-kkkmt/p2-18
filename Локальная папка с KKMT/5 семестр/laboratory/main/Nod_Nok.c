#include "pch.h"

int gcd(int a, int b){
  return a % b ? gcd(b, a % b) : b;
}

int nod_nok(){
    system("cls");
  int a, b;

  printf("������� ��� ����������� ����� > ");
  scanf("%i%i", &a, &b);

    printf("���(%i,%i) = %i\n", a, b, gcd(a, b));
    printf("���(%i,%i) = %li\n", a, b, (long) a * b / gcd(a, b));
    system("pause");
    return 0;

}

