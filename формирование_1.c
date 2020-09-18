#include <stdio.h>
int main()
{
    int a[100];
    int n, i=1;
    scanf("%i",&n);
    a[0]=1;
    for (i=1; i<n; ++i)
    a[i]=a[i-1]+2;
    for (i=0; i<n; ++i)
    printf("%i\n",a[i]);
    return 0;
}
