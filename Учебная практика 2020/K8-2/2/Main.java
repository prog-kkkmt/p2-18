package com.company;

//Задание 2. Array113. Дан массив A размера N.
//Упорядочить его по возрастанию методом сортировки простым
//выбором: найти максимальный элемент массива и поменять его
//местами с последним (N-1 м) элементом; выполнить описанные
//действия N  1 раз, каждый раз уменьшая на 1 количество
//анализируемых элементов и выводя содержимое массива.
//test input 10 3 4 8 7 6 5 4 3 2 1

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner consoleScanner = new Scanner(System.in);
        System.out.println("Enter N");
        int n = consoleScanner.nextInt();
        int[] array = new int[n];
        int max = 0;
        int tmp;

        for(int i = 0; i < n;i++){
            array[i] = consoleScanner.nextInt();//scanner.nextInt();
        }

        for(int i = 0; i < n-2;i++){
            max = i;
            for(int j = i + 1; j < n - 1; j++){
                if(array[j] > array[max]){
                    max = j;
                }
                for (int k : array) {
                    System.out.print(k + " ");
                }
                System.out.println(" ");
            }
            System.out.println(" ");
            tmp = array[i];
            array[i] = array[max];
            array[max] = tmp;
        }


    }
}
