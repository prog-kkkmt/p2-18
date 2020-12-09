package com.company;
//Выполнил: Безбородов Константин П2-18
//М. Э. Абрамян (Южный федеральный университет), 1998–2020
//http://ptaskbook.com/ru/tasks/array.php

//Задание 5. Matrix56. Дана матрица размера M x N (N — четное число). Поменять местами
//левую и правую половины матрицы.

/*
4 4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
*/

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        int m = 10;//default var
        int n = 10;//default var
        int tmp;

        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();
        int[][] arr = new int[m][n];


        //input
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n;j++) {
                arr[i][j] = scanner.nextInt();
            }
        }

        //work
        for(int i = 0; i < m; i++){
            for(int j = 0, k = n - 1; j < n / 2; k--, j++) {
                tmp = arr[i][k];
                arr[i][k] = arr[i][j];
                arr[i][j] = tmp;
            }
        }

        //output
        for(int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(+ arr[i][j] + " ");
            }
            System.out.println(" ");

        }
    }
}
