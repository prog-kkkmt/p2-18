//for 4
/*http://www.ptaskbook.com/ru/tasks/for.php*/
/*Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, …, 10 кг конфет.*/

package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        int i;

        System.out.println("a = ");
        int a = in.nextInt();

        for(i=1;i<=10;i++){
            System.out.println("cost " + i + "kg = " + (a*i));
        }
    }
}
