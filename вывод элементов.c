#include <stdio.h>
int main()
{
    int a[100];
    int n, i;
    scanf("%i",&n);
    for (i=0; i<n; ++i){
    scanf("%i",&a[i]);
    }
    for (i=n-1; i>=0; --i)
    printf(" %i\n",a[i]);
}
