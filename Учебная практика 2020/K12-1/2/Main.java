package com.company;
//Выполнил Безбородов П2-18

//Задание 2. https://pythontutor.ru/lessons/sets/problems/number_of_coincidental/
//Задача «Количество совпадающих чисел»
//Условие. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как
//в первом списке, так и во втором.

import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
        //input 1
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        scanner = new Scanner(input);
        int counter = 0;

        //добавить в сет значения(сет хранит только уникальные)
        Set<Integer> set1 = new HashSet<>();
        while(scanner.hasNextInt()){
            set1.add(scanner.nextInt());
        }
        //input 2
        scanner = new Scanner(System.in);
        input = scanner.nextLine();
        scanner = new Scanner(input);

        //добавить в сет значения(сет хранит только уникальные)
        Set<Integer> set2 = new HashSet<>();
        while(scanner.hasNextInt()){
            set2.add(scanner.nextInt());
        }
        
        //если совпдают counter++
        for (Integer integer : set1) {
            for (Integer integer1 : set2) {
                if(integer == integer1){
                    counter++;
                }
            }
        }
        System.out.println(counter);
    }
}
