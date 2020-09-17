/* Programming Taskbook. Электронный задачник по программированию
(c)  М. Э. Абрамян (Южный федеральный университет), 1998–2020 */
// Одномерные массивы
// http://ptaskbook.com/ru/tasks/array.php
/** Array1. Дано целое число N (>0). Сформировать и вывести целочисленный массив размера N, содержащий
N первых положительных нечетных чисел: 1, 3, 5, ... . */
/** Решение. Гусятинер Л.Б., МГОТУ ККМТ, 17.09.2020 */
#include <stdio.h>
#include <stdlib.h>

int main() {
	size_t n;
	scanf("%d", &n);
	int *pv = (int *)malloc(n * sizeof(int));
	for (size_t i = 0; i < n; i++)
        *(pv + i) = i * 2 + 1;
	for (size_t i = 0; i < n; i++) {
	    printf("%d", *(pv + i));
        if (i < n - 1)
            printf(",");
    }
    printf("\n");
    free(pv);

	return 0;
}
