// Описать функцию MinElem(A, N) целого типа,
//находящую минимальный элемент целочисленного массива
//A размера N. С помощью этой функции найти минимальные
//элементы массивов A, B, C размера NA, NB, NC соответственно.

#include <stdio.h>
#include <stdlib.h>

MinElem(int* a, int n){
    int answer = a[0]; // изначально минимальное число = первому элементу массива
    for(int i = 0; i < n; ++i){
        if(answer > a[i]){ //поиск мин значения
            answer = a[i];
        }
    }
    return answer;
}

int main()
{
//для данной прогрыммы не стал реализововать ввод данных с клавиатуры, для удобства проверки.
int a[5] = {5, 3, 1, 6, 7}; //исходные данные
int b[3] = {6, 5, 3};
int c[2] = {1, -5};

printf("first array min = %d \n", MinElem(a, 5));
printf("secound array min = %d \n", MinElem(b, 3));
printf("first array min = %d \n", MinElem(c, 2));

return 0;
}
