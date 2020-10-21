#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
    int n=0;
    char a[15];
    gets(a);
    for (int i=0;i<15;i++)
    {
        if (a[i]==' ')
        {
            printf ("%d ",i);
            n++;
        }         
    }
    if (n==0)
        printf ("-");
    return 0;
}
