package com.company;

//Задание 1. Array112. Дан массив A размера N.
//Упорядочить его по возрастанию методом сортировки
//простым обменом («пузырьковой» сортировкой):
//просматривать массив, сравнивая его соседние элементы
//(A0 и A1, A1 и A2 и т. д.) и меняя их местами,
//если левый элемент пары больше правого; повторить описанные
//действия N  1 раз. Для контроля за выполняемыми действиями
//выводить содержимое массива после каждого просмотра.
//Учесть, что при каждом просмотре количество анализируемых
//пар можно уменьшить на 1.
//test input 10 3 4 8 7 6 5 4 3 2 1

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner consoleScanner = new Scanner(System.in);
        System.out.println("Enter N");
        int n = consoleScanner.nextInt();
        int[] array = new int[n]; //{3,4,8,7,6,5,4,3,2,1};

            for(int i = 0; i < n;i++){
                array[i] = consoleScanner.nextInt();//scanner.nextInt();
        }

        for(int i = 0; i < array.length;i++){
            for(int j = i; j < array.length;j++){
                if(array[i] < array[j]){
                    //swap
                    array[i] += array[j];
                    array[j] = array[i] - array[j];
                    array[i] = array[i] - array[j];
                }
                //output
                for (int k : array) {
                    System.out.print(k + " ");
                }
                System.out.println(" ");
            }
            System.out.println(" ");

        }

    }
}
