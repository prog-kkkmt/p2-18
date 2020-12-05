package com.company;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

//Задание 1
//Задача «Больше своих соседей»
//Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух
//своих соседей, и выведите количество таких элементов. Крайние элементы списка никогда
//не учитываются, поскольку у них недостаточно соседей.
public class Main {

    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>(); // создание листа

        Scanner consoleScanner = new Scanner(System.in); //сканнер для работы с консолью
        String input = consoleScanner.nextLine();//считать строку чисел
        Scanner scanner = new Scanner(input);//создать сканнер для работы с вводимой строкой

        int counter = 0;//перменная с ответом

        while (scanner.hasNextInt()){// добавить вводимые числа в лист
            list.add(scanner.nextInt());
        }
        //обработка листа, если число больше соседей, счетчик ответа ++, первое и последнее не проверяет, тк нет соседей.

        for(int i = 1; i < list.size() - 1; i++){
            if(list.get(i) > list.get(i-1) && list.get(i) > list.get(i+1)){
                counter++;
            }
        }

        System.out.println(counter);// вывод ответа

    }
}
