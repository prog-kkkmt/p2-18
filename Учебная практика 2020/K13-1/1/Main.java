package com.company;
//Выполнил Безбородов П2-18

import java.util.Scanner;

//Задание 1. https://stepik.org/lesson/193753/step/4?unit=168148
//Вывести чётные
//Необходимо вывести все четные числа на отрезке [a; a * 10].
//Sample Input:
//2
//Sample Output:
//(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());//считываем n
        //если n положительное
        if(n > 0) {
            for (int i = n; i <= n * 10; i += 2) {
                System.out.print(i + " ");
            }
        }
        //если n отрицательное
        else{
            for(int i = n; i >= n * 10; i -= 2){
                System.out.print(i + " ");
            }
        }
    }
}
