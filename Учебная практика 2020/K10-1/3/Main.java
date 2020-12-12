package com.company;

//////Выполнил: Безбородов Константин П2-18
//////М. Э. Абрамян (Южный федеральный университет), 1998–2020
//////http://ptaskbook.com/ru/tasks/array.php

//Задание 3. Func10. Описать функцию IsSquare(K) логического типа, возвращающую True,
//если целый параметр K (> 0) является квадратом некоторого целого числа, и False
//в противном случае. С ее помощью найти количество квадратов в наборе из 10 целых
//положительных чисел.

import java.util.Scanner;

public class Main {
//функция проверки
    public static boolean IsSquare(int  k){
        if(Math.sqrt(k) % 1 == 0){
            return true;
        }else {
            return false;
        }

    }


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        scanner = new Scanner(input);
        while(scanner.hasNextInt()){
            System.out.println(IsSquare(scanner.nextInt()));
        }
    }
}
