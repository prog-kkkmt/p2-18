package com.company;
//Задание 2. https://pythontutor.ru/lessons/lists/problems/num_equal_pairs/
//Задача «Количество совпадающих пар»
//Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
//Считается, что любые два элемента, равные друг другу образуют одну пару, которую
//необходимо посчитать.
//my Test 1 2 3 1 3 1 
//answer 2

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        //Ввод с консоли
        Scanner consoleScanner = new Scanner(System.in);
        String consoleInput = consoleScanner.nextLine();
        Scanner stringScanner = new Scanner(consoleInput);

        //создание переменных
        Integer tmp;
        Integer counter = 0;
        Integer tmpCounter;

        //создание листов
	    List<Integer> list = new ArrayList<>();
	    List<Integer> checked = new ArrayList<>();

	    //Добавление в лист элементов с консоли
        while(stringScanner.hasNextInt()){
            list.add(stringScanner.nextInt());
        }

        //Бежит по всем элементам вложенным циклом
	    for(int i = 0; i < list.size();i++){
            tmp = list.get(i); //tmp перменная для текущего искомого элемента
            tmpCounter = 0;// сколько нашло совпадений
	        for(int j = 0; j < list.size();j++){
	            if(tmp == list.get(j) && !checked.contains(tmp)){
	                tmpCounter++;// если находит совпадение, и если мы не проверяли это число, увеличить счетчик совпадений
                }
            }

	        counter += tmpCounter / 2;//счетчик совпадений / 2 = кол-во пар
	        checked.add(tmp);//добавить элемент в проверенные
        }
	    System.out.println(counter); //вывод ответа

    }
}
