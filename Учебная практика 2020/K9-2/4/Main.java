package com.company;

//Выполнил: Безбородов Константин П2-18
//М. Э. Абрамян (Южный федеральный университет), 1998–2020
//http://ptaskbook.com/ru/tasks/array.php

//Задание 4. Matrix3. Даны целые положительные числа M, N и набор из M чисел. Сформировать
//матрицу размера M x N, у которой в каждом столбце содержатся все числа из исходного
//набора (в том же порядке).

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int m = 10;//default var
        int n = 10;//default var

        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();
        int[][] arr = new int[m][n];



        for(int i = 0; i < m; i++){
            for(int j = 0; j < n;j++) {
                arr[i][j] = scanner.nextInt();
            }
        }
        for(int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(+ arr[i][j] + " ");
            }
            System.out.println(" ");
        }
    }
}
