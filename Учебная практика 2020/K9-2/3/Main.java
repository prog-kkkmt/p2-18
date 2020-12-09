package com.company;

//Задание 3. Array58. Дан массив A размера N. Сформировать новый массив B того же размера по
//следующему правилу: элемент B[K] равен сумме элементов массива A с номерами от 0 до K.
//test input 5 3 5 7 9 11
//test out 3 8 15 24 35

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        //Входные данные
        int n = 100;
        Scanner scanner = new Scanner(System.in);
        int[] arr = new int[n];
        n = scanner.nextInt();

        int[] answerArr = new int[n];

        for(int i = 0; i < n;i++){
            arr[i] = scanner.nextInt();
        }

        // B[i] равен сумме элементов массива A с номерами от 0 до i.
        for(int i = 0; i < n; i++){
            for(int k = 0; k < i+1; k++){
                answerArr[i] += arr[k];
            }
        }

        for (int i : answerArr) {
            System.out.println(i);
        }

    }
}
