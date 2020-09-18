/*Найти сумму 10 элементов массива. Слесарев А.М. 18.09.20*/
#include <stdio.h>
 
int main()
{
  int a[10],i,sum=0;
  for (i = 0; i < 10; i++)
  {
    scanf ("%d", &a[i]);
    sum+=a[i];
  }
  printf ("Сумма элементов массива:%d", sum);
}