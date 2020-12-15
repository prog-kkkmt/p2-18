package com.company;
//Выполнил Безбородов П2-18

//Задание 1. https://pythontutor.ru/lessons/sets/problems/number_of_unique/
//Задача «Количество различных чисел»
//Условие. Дан список чисел. Определите, сколько в нем встречается различных чисел.

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
        //input
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        scanner = new Scanner(input);
        //добавить в сет значения(сет хранит только уникальные)
        Set<Integer> uniq = new HashSet<>();
        while(scanner.hasNextInt()){
            uniq.add(scanner.nextInt());
        }
        System.out.println(uniq.size());


    }
}
