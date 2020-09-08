#include <stdio.h>
#include <stdlib.h>

#define MAXN 100

int main()
{
    int b0 = 0, q = 0, n;
    int mas[MAXN];

    printf("Enter n\n");
    scanf("%d", &n);

    printf("Enter b0\n");
    scanf("%d", &b0);

    printf("Enter q\n");
    scanf("%d", &q);

    mas[0] = b0;

    for(int i = 1; i < n; ++i){
        mas[i] = mas[i-1] * q;
    }

    printf("ANSWR: %d", mas[n-1]);
    return 0;
}
