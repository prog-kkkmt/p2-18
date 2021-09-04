// begin 4
/*http://www.ptaskbook.com/ru/tasks/begin.php*/
/*Дан диаметр окружности d. Найти ее длину L = π·d. В качестве значения π использовать 3.14.*/


package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        double p = 3.14;
        double L;
        System.out.println("d = ");
        Scanner in = new Scanner(System.in);
        int d = in.nextInt();
        L = d * p;
        System.out.println("L= " + L);

    }
}
