//Даны целые положительные числа M и N. Сформировать целочисленную матрицу размера M × N,
// у которой все элементы I-й строки имеют значение 10·I (I = 1, …, M).


public class Main {

    public static void main(String[] args) {
        int m = 5,n = 3; // размеры матрицы
        int arr[][] = new int [m][n];//создание матрицы m  X n
        for(int i = 0; i < m;++i){
            for(int j = 0; j < n; ++j){
                arr[i][j] = i*10; // заполнение матрицы в соответсвии с условием
            }
        }
        for(int i = 1; i < m;++i) {
            for (int j = 0; j < n; ++j) {
                System.out.print(arr[i][j] + " "); //вывод матрицы
            }
            System.out.println(" ");

        }
    }
}
