// while 4
/*http://www.ptaskbook.com/ru/tasks/while.php*/
/*Дано целое число N (> 0). Если оно является степенью числа 3, то вывести true, если не является — вывести false.*/

package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        System.out.println("a = ");

        int a = in.nextInt();

        while(a%3 == 0){
            a/=3;
        }

        if (a==1){
            System.out.println("True");
        }

        else{
            System.out.println("False");
        }

    }

    }
