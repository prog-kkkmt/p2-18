// integer 4
/*http://www.ptaskbook.com/ru/tasks/integer.php*/
/* Даны целые положительные числа A и B (A > B). На отрезке длины A размещено
максимально возможное количество отрезков длины B (без наложений).
Используя операцию деления нацело, найти количество отрезков B, размещенных на отрезке A.*/



package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        System.out.println("a =");

        int a = in.nextInt();

        System.out.println("b =");

        int b = in.nextInt();

        if (b>a){
            System.out.println("Uncorrect. b>a");
        }

        else{

           int res = a/b;

           System.out.println(res);

        }
    }
}
