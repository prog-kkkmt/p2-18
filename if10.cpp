#include <stdio.h>
int main(void)
{
   int a, b;

   scanf ("%d", &a); // ���� A � B
   scanf ("%d", &b);

   if (a!=b) a=b=a+b; // ���� � �� ����� b, �� ��������� ��������, ���� �����, �� ���� ��������� 0
   else a=b=0;

   printf("a=%d\n b=%d\n",a,b); // �����
   return 0;
}

