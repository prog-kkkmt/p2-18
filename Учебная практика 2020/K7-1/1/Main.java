package com.company;

//С клавиатуры вводятся строки, последовательность заканчивается точкой.
//Выведите буквы введенных слов в верхнем регистре, разделяя их пробелами.

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);//сканнер для ввода

        String[] strings = new String[200]; //максимальное кол во строк
        int i = 0;//индекс для цикла

        while (true){
            strings[i] = scanner.nextLine();//считывать строки

            if(strings[i].contains(".")){//если нашел . увеличить кол-во строк(которые мы ввели до .) и остановить while
                i++;
                break;
            }

            i++;//если не нашли . в строке просто ++ счетчику
        }

        for(int j = 0; j < i; j++){//обработка всех строк
            char[] charString = strings[j].toCharArray(); // создание массива char из j-ой  строки

            for(int k = 0; k < charString.length; k++){
                System.out.print(Character.toUpperCase(charString[k]) + " ");// вывод в верхнем регистре + пробел
            }
        }
    }
}
