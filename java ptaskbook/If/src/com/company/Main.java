// if 4
/*http://www.ptaskbook.com/ru/tasks/if.php*/
/*Даны три целых числа. Найти количество положительных чисел в исходном наборе.*/


package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        int counter = 0;

        Scanner in = new Scanner(System.in);
        System.out.println("a = ");
        int a = in.nextInt();

        System.out.println("b = ");
        int b = in.nextInt();

        System.out.println("c = ");
        int c = in.nextInt();

        if (a>0){
            counter +=1;
        }
        if (b>0){
            counter +=1;
        }
        if(c>0){
            counter +=1;
        }
        System.out.println(counter);
    }
}
