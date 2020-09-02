//Дано целое число N и набор из N целых чисел.
//Найти количество элементов, расположенных перед первым минимальным элементом.
#include <stdio.h>
int main(void)
{
    int minnum,i,n,r,min;

    printf("N:");
    scanf("%i", &n);

    for (i=1; i<=n; ++i){
        printf("%i>",i);
        scanf("%i", &r);

        if ((r<min)||(i==1)){
            min=r;
            minnum=i;
        }
    }
    printf("%i\n",minnum-1);
    return 0;
}
