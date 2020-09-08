// Дан файл целых чисел. Создать два новых файла, первый из которых содержит положительные числа из исходного файла (в обратном порядке),
// а второй — отрицательные (также в обратном порядке).
// Если положительные или отрицательные числа в исходном файле отсутствуют, то соответствующий результирующий файл оставить пустым.
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
// Не доделал, не успел.
int main()
{
setlocale (0,"");
    FILE *Dano, *Pol, *Otr;
     int x, prov; //a, b,
    printf("Ввели данные до запуска программы?\n");
     printf("1 - Да.\n0 - Нет.\n");
    scanf("%d", prov);
     if ( prov = 1 )
    {
        Dano = fopen("Dano.txt", "r");
        for(int i = 0; i < n; i++)
        {
            fscanf(Dano, "%d", x);

        if ( x > 0 )
        {
            Pol = fopen("Pol.txt", "w");
            fprintf(Pol, "%d", x);
        }
        else if ( x < 0)
        {
            Otr = fopen("Otr.txt", "w");
            fprintf(Pol, "%d", x);
        }
        else
        {
            printf("\nВ вводных данных кроме нуля (нулей) ничего нет ;c");
        }
        }
    }
    else
    {
        printf("\nНу значит запиши c;\n");
        return 0;
    }

}
