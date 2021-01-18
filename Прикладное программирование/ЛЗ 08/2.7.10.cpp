/*Выполнили: Короленко И.Р., Кузнецов М.С., Слесарев А.М.
  Группа: ККМТ П2-18

Реализуйте функцию swap_min, которая принимает на вход двумерный массив целых чисел,
 ищет в этом массиве строку, содержащую наименьшее среди всех элементов массива значение,
 и меняет эту строку местами с первой строкой массива.
Подумайте, как обменять строки массива, не обменивая элементы строк по-отдельности.
 Требования к реализации: при выполнении этого задания вы можете определять любые вспомогательные функции.
 Вводить или выводить что-либо не нужно. Реализовывать функцию main не нужно.
*/

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

void swap_min(int *m[], unsigned rows, unsigned cols){
    int buf, min = m[0][0];
    for (int i = 0; i<rows; i++)
        for (int j = 0; j<cols; j++)
            if (m[i][j] < min){
                buf = i;
                min = m[i][j];
            }
    int *buf1 = m[buf];
    m[buf] = m[0];
    m[0] = buf1;
}

int main(){
    int rows, cols;
    int *mas[rows][cols];
    int i, j;
    srand(time(NULL));
    cin >> rows >> cols;
    for (i = 0; i < rows; i++){
        for (j = 0; j < cols; j++){
            mas[i][j] = rand() % 10;
            cout << mas[i][j] << "\t";
        }
        cout << endl;
    }

    return 0;
}

