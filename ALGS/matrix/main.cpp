#include <iostream>

using namespace std;

int main()
{
//Даны целые положительные числа M и N. Сформировать целочисленную матрицу размера M × N,
// у которой все элементы I-й строки имеют значение 10·I (I = 1, …, M).

        int m, n; // размеры матрицы
        cin >> m;
        cin >> n;
        int arr[m][n]; //создание матрицы m  X n
        for(int i = 0; i < m;++i){
            for(int j = 0; j < n; ++j){
                arr[i][j] = i*10; // заполнение матрицы в соответсвии с условием
            }
        }
        for(int i = 1; i < m;++i) {
            for (int j = 0; j < n; ++j) {
                cout << arr[i][j] <<  " "; //вывод матрицы
            }
            cout << "\n";

        }
    }


