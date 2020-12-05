package com.company;

//?Известно, что для логина часто не разрешается использовать строки содержащие пробелы.
//Но пользователю нашего сервиса особенно понравилась какая-то строка.
//Замените пробелы в строке на символы нижнего подчеркивания, чтобы строка
//могла сгодиться для логина. Если строка состоит из одного слова, менять ничего не нужно.
//Sample Input: python sila
//Sample Output: python_sila

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);//считать строку
        String input = scanner.nextLine();

        if (input.contains(" ")) {// если есть пробелы в строке
            input = input.replace(" ", "_");//заменить на _
        }

        System.out.println(input);//вывод
    }
}
