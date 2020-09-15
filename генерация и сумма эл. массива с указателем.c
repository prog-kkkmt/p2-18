#include <stdio.h>
#include <time.h>
#include <locale.h>

int sum (int *a, int n)
{
    int s = 0;
    for (int i = 0; i < n; i++)
    {
        s += a[i];
    }
    return s;
}
int main()
{
    srand(time(NULL));
    setlocale(0,"");
    int R[9];
    printf("Сгенерированный массив:\n");
    for (int i = 0; i < 9; i++)
    {
        R[i]=rand()%10;
        printf("%d ", R[i]);
    }
    printf("\nСумма сгенерированных выше элементов:");
    printf(" %d", sum(R, 9));

}
