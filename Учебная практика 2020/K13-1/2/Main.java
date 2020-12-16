package com.company;
//Выполнил Безбородов П2-18

//Задание 2. https://stepik.org/lesson/193753/step/5?unit=168148
//Убывающий ряд.
//С клавиатуры вводятся целые числа a > b. Выведите убывающую последовательность чисел
//по одному числу в строке.
//Sample Input:
//-2
//-8
//Sample Output:
//-2
//-3
//-4
//-5
//-6
//-7

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int a = Integer.parseInt(scanner.nextLine());//считываем a
        int b = Integer.parseInt(scanner.nextLine());//считываем b

        //если n положительное
        if(a > 0) {
            for (int i = b; i != a; i--) {
                System.out.println(i + " ");
            }
        }
        //если n отрицательное
        else{
            for(int i = a; i > b; i--){
                System.out.println(i + " ");
            }
        }
    }
}

