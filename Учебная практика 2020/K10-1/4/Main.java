package com.company;

//Func33. Описать функцию SortInc3(X), меняющую содержимое списка X из трех
//вещественных элементов таким образом, чтобы их значения оказались упорядоченными по
//возрастанию (функция возвращает None). С помощью этой функции упорядочить по
//возрастанию два данных списка X и Y.

import java.util.Comparator;
import java.util.LinkedList;

//создание компаратора для сортировки
class vozrSortComp implements Comparator<Integer>{
    @Override
    public int compare(Integer o1, Integer o2) {
        if(o1 < o2){
            return -1;
        }else if(o1 > o2){
            return 1;
        }
        return 0;
    }
}
//создание функции требуемой в задании
class Worker{
    public static LinkedList<Integer> SortInc3(LinkedList<Integer> list){
        vozrSortComp comp = new vozrSortComp();
        list.sort(comp);
        return list;
    }
}

public class Main {

    public static void main(String[] args) {
        //входные данные
        LinkedList <Integer> list = new LinkedList<>();
        list.add(1);
        list.add(16);
        list.add(3);

        LinkedList <Integer> list2 = new LinkedList<>();
        list2.add(99);
        list2.add(1123);
        list2.add(1);

        //вывод входных данных
        System.out.println("first not Sorted");

        for (Integer integer : list) {
            System.out.println(integer);
        }

        System.out.println("Secoud  not Sorted");

        for (Integer integer : list2) {
            System.out.println(integer);
        }

        //выходные данные
        LinkedList <Integer> listAnswer = new LinkedList<>();
        listAnswer = Worker.SortInc3(list);

        LinkedList <Integer> listAnswer2 = new LinkedList<>();
        listAnswer2 = Worker.SortInc3(list2);
        
        //Вывод выходных данных
        
        System.out.println("first Sorted");

        for (Integer integer : listAnswer) {
            System.out.println(integer);
        }

        System.out.println("Secoud Sorted");

        for (Integer integer : listAnswer2) {
            System.out.println(integer);
        }
    }
}
