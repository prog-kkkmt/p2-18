/* Programming Taskbook. Электронный задачник по программированию
(c)  М. Э. Абрамян (Южный федеральный университет), 1998–2020 */
// Двумерные массивы (матрицы)
// http://ptaskbook.com/ru/tasks/matrix.php
/* Matrix1. Даны целые положительные числа M и N. Сформировать целочисленную матрицу размера M * N,
у которой все элементы I-й строки имеют значение 10*I (I = 1, ..., M). */
/* Решение. Гусятинер Л.Б., МГОТУ ККМТ, 17.09.2020 */
#include <stdio.h>
#include <stdlib.h>

int main() {
	size_t m, n;
	scanf("%d%d", &m, &n);
	int **mat = (int **)malloc(m * sizeof(int));
	for (size_t i = 0; i < m; i++)
        mat[i] = (int *)malloc(n * sizeof(int));
	for (size_t i = 0; i < m; i++) {
		int elem = 10 * i;
		for (size_t j = 0; j < n; j++)
			mat[i][j] = elem;
	}
	for (size_t i = 0; i < m; i++) {
		for (size_t j = 0; j < n; j++) {
			printf("%d", mat[i][j]);
			if (j < n - 1)
				printf("\t");
		}
		printf("\n");
	}

	for (size_t i; i < m; i++)
        free(mat[i]);
    free(mat);

	return 0;
}
