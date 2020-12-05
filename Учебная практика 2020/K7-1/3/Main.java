package com.company;

//?Уберите точки из введенного IP-адреса. Выведите сначала четыре числа через пробел,
//а затем сумму получившихся чисел.
//Sample Input: 192.168.0.1
//Sample Output:
//192 168 0 1
//361

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner consoleScanner = new Scanner(System.in);// сканнер для консоли

        String input = consoleScanner.nextLine().replace(".", " ");// переменная для ввода с консоли и замена точек на пробелы
        System.out.println(input);// вывод без точек
        int answer = 0;//переменная для суммы

        Scanner scanner = new Scanner(input);// сканнер для работы со строкой

        while(scanner.hasNextInt()){//пока есть целые числа в строке
            answer += scanner.nextInt(); //прибавлять к переменной ответа целые числа из строки
        }

        System.out.println(answer);//вывод ответа
    }
}
