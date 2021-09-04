//case 4
/*http://www.ptaskbook.com/ru/tasks/case.php*/
/* Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — февраль и т. д.).
 Определить количество дней в этом месяце для невисокосного года.*/

package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner in = new Scanner(System.in);

        System.out.println("d = ");
        int d = in.nextInt();

        switch (d){
            case (1):
                System.out.println("31 days");
                break;
            case (2):
                System.out.println("28 days");
                break;
            case (3):
                System.out.println("31 days");
                break;
            case (4):
                System.out.println("30 days");
                break;
            case (5):
                System.out.println("31 days");
                break;
            case (6):
                System.out.println("30 days");
                break;
            case (7):
                System.out.println("31 days");
                break;
            case (8):
                System.out.println("31 days");
                break;
            case (9):
                System.out.println("30 days");
                break;
            case (10):
                System.out.println("31 days");
                break;
            case (11):
                System.out.println("30 days");
                break;
            case (12):
                System.out.println("31 days");
                break;
            default:
                System.out.println("uncorrect number");
                break;
        }
    }
}
