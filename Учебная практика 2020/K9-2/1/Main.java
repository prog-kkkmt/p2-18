package com.company;

/*Задание 1. Array55. Дан целочисленный массив A размера N (<= 15). Переписать в новый целочисленный
массив B все элементы с нечетными порядковыми номерами (1, 3, ...) и вывести размер
полученного массива B и его содержимое. Условный оператор не использовать.*/

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	//входные данные
        int n = 15;
        Scanner scanner = new Scanner(System.in);
        int[] arr = new int[n];
        n = scanner.nextInt();

        int[] answerArr = new int[n/2];


        for(int i = 0; i < n;i++){
            arr[i] = scanner.nextInt();
        }
	
	//добавление в новый массив все значения не четных индексов
        for (int i = 1, j = 0; i < n; i += 2, j++){
            answerArr[j] = arr[i];
            System.out.println(answerArr[j]);
        }

        System.out.println("size: " + answerArr.length);


    }
}
