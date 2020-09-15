#include <stdio.h>
void swap (int *pa, int *pb)
{
    int t = *pa;
    *pa = *pb;
    *pb = t;
}
int main()
{
    int a = 3, b = 4;
    swap (&a,&b);
    printf ("%d %d", a, b);
    return 0;
}
