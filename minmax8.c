//ƒано целое число N и набор из N целых чисел. Ќайти номера первого и последнего минимального элемента из данного набора
//и вывести их в указанном пор€дке.
#include <stdio.h>
int main(void)
{
    int i,n,ni,minnum,maxnum,min,max;
    printf("N:");
    scanf("%i", &n);
    for (i=1;i<=n;++i){
        printf("%i>",i);
        scanf("%i", &ni);
        if ((i==1)||(ni<=min)){
            min=ni;
            minnum=i;
        }
        if ((i==1)||(ni>max)){
            max=ni;
            maxnum=i;
        }
    }
    printf("%i  %i\n", minnum,maxnum);
    return 0;
}
