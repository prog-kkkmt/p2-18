package com.company;

//Выполнил: Безбородов Константин П2-18
//М. Э. Абрамян (Южный федеральный университет), 1998–2020
//http://ptaskbook.com/ru/tasks/array.ph

//Задание 2. Array57. Дан целочисленный массив A размера N. Переписать в новый целочисленный массив B
//того же размера вначале все элементы исходного массива с четными номерами,
//а затем — с нечетными:
//A[0], A[2], A[4], A[6], ..., A[1], A[3], A[5], ... .
//Условный оператор не использовать.

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        //Входные данные
        int n = 100;
        Scanner scanner = new Scanner(System.in);
        int[] arr = new int[n];
        n = scanner.nextInt();
        int counter = 0;

        int[] answerArr = new int[n];

        for(int i = 0; i < n;i++){
            arr[i] = scanner.nextInt();
        }

        //Записать четнеые
        for(int i = 0, k = 0; k < n; i++, k+=2){
            answerArr[i] = arr[k];
            counter++;
        }
        //Записать не четные
        for(int i = counter, k = 1; k < n; i++, k+=2){
            answerArr[i] = arr[k];
        }

        for (int i : answerArr) {
            System.out.println("out: " + i );
        }

        System.out.println("size: " + answerArr.length);


    }
}
