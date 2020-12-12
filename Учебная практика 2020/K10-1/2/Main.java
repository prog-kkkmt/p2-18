package com.company;

////Выполнил: Безбородов Константин П2-18
////М. Э. Абрамян (Южный федеральный университет), 1998–2020
////http://ptaskbook.com/ru/tasks/array.php

//Задание 2. Func6. Описать функцию SumRange(A, B) целого типа, находящую сумму всех целых
//чисел от A до B включительно (A и B — целые). Если A > B, то функция возвращает 0.
//С помощью этой функции найти суммы чисел от A до B и от B до C, если даны числа A, B, C.

import java.util.Scanner;

public class Main {
    
        static public int SumRange(int a, int b){
            int answer = 0;
            if(a > b){
                return answer;
            }else{
                for(int i = a; i < b + 1;i++){
                    answer += i;
                }
            }
            return answer;
        }

    public static void main(String[] args) {
        //input
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c =  scanner.nextInt();

	System.out.println("range (a,b): "+ SumRange(a,b)+ "\n"+ "range(b,c): " + SumRange(b,c));
    }
}
