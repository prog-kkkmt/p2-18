//Array7°. Дан массив размера N. Вывести его элементы в обратном порядке.
#include <stdio.h>
#include <stdlib.h>
#define MAX 1000
int main()
{
 int mas[MAX];
 int i, n;
 scanf("%d", &n);
 for (i=0; i<n; i++)
      scanf("%d", &mas[i]);
 for (i=n-1; i>=0; i--)
      printf("%d", mas[i]);

    return 0;
}
