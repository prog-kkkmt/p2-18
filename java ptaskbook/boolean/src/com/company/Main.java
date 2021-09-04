// boolean 4
/*http://www.ptaskbook.com/ru/tasks/boolean.php*/
/*Даны два целых числа: A, B. Проверить истинность высказывания: «Справедливы неравенства A > 2 и B ≤ 3*/

package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        System.out.println("a = ");
        int a = in.nextInt();

        System.out.println("b = ");
        int b = in.nextInt();

        boolean m = ((a > 2) & (b <=3));

        System.out.println(m);

    }
}
