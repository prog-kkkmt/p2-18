package com.company;

//Выполнил: Безбородов Константин П2-18
//М. Э. Абрамян (Южный федеральный университет), 1998–2020
//http://ptaskbook.com/ru/tasks/array.php

/*
Задание 6. Matrix88. Дана квадратная матрица порядка M. Обнулить элементы матрицы,
лежащие ниже главной диагонали. Условный оператор не использовать.
*/


import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        int m = 10;//default var
        int n = 10;//default var

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
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                arr[i][j] = 0;
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
