package com.company;
//Выполнил Безбородов П2-18
//Задание 3. https://pythontutor.ru/lessons/sets/problems/sets_intersection/
//Задача «Пересечение множеств»
//Условие. Даны два списка чисел. Найдите все числа, которые входят как в первый,
//так и во второй список и выведите их в порядке возрастания.

import java.util.*;

public class Main {

    public static void main(String[] args) {
        //input 1
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        scanner = new Scanner(input);

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

        SortedSet<Integer> out = new TreeSet<>();
        //найти совпадения и добавить в сортированный сет
        for (Integer integer : set1) {
            for (Integer integer1 : set2) {
                if(integer == integer1){
                    out.add(integer);
                    break;
                }
            }
        }
        //вывод сортированного сета(по умолчанию выводит значения по возрастанию)
        for (Integer integer : out) {
            System.out.println(integer);
        }
    }
}
