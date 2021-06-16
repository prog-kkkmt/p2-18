#include <windows.h>
#include <stdlib.h>
#include <locale.h>

void main()
{
    setlocale(0,"");
        int i,*pm, max=0, nmax=0, *tmp, *p[10], flag,n;
            printf("Заполните массив: ");
                scanf("%d",&n);
                    int mas[n];
                pm=&mas;
            for(i=0; i<n; i++)
                {
                    scanf ("%d", pm);
                    pm++;
                }
            pm-=n;
                    max=mas[0];
                        nmax=0;
            for(i=0;i<n;i++)
                {
                    if(*pm > max)
                    {
                        nmax=i;
                        max=*pm;
                    }
                    pm++;
            }
                    pm-=n;
        printf ("Максимальный элемент: ");
            printf ("%d", max);
                pm-=n;
   for (i=0; i<10; i++)
            {
                p[i]=&mas[i];
            }
do {
            flag=0;
        for(i=1;i<n;i++)
        {
            if (*p[i]>*p[i-1])
            {
                tmp=p[i];
                p[i]=p[i-1];
                p[i-1]=tmp;
                flag=1;
            }
        }
    }
        while (flag);
printf("\nОтсортированный массив: ");
    for (i=0; i<n; i++)
    {
        printf ("%d ", *p[i]);
    }
}



