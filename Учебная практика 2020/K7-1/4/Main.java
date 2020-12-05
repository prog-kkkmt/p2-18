package com.company;

//Задание 4.
//Программист логирует программу, чтобы хорошо знать,
//как она себя ведет (эта весьма распространенная и важная практика).
//Он использует разные типы сообщений для вывода ошибок (error),
//предупреждений (warning), информации (info) или подробного описания (verbose).
//Сообщения отличаются по внешнему виду. Назовем модификаторами такие символы,
//которые отличают сообщения друг от друга, позволяя программисту понять, к какому
//из типов относится сообщения. Модификаторы состоят из двух одинаковых символов
//и записываются по разу в начале и в конце строки.
//
//@@ обозначает ошибку
//!! обозначает предупреждение
//// обозначает информационное сообщение
//** обозначает подробное сообщение
//Напишите программу, которая принимает строки до точки и выводит,
//какого типа это сообщение. Если сообщение не содержит модификаторов,
//проигнорируйте его.
//
//Sample Input:
//!! cannot resolve this method !!
//@@ invalid type @@
//@@ StackOverFlowException @@
//// here I change the variables name //
//** this class is used for operating with the database, including CRUD operations and registering new users **
//error on line 42
//// TODO: optimize recursive calls //
//.
//
//Sample Output:
//предупреждение
//ошибка
//ошибка
//информация
//подробное сообщение
//информация

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);//сканнер для ввода

        String[] strings = new String[200]; //максимальное кол во строк
        int i = 0;//индекс для цикла

        while (true) {
            strings[i] = scanner.nextLine();//считывать строки

            if (strings[i].contains(".")) {//если нашел . увеличить кол-во строк(которые мы ввели до .) и остановить while
                i++;
                break;
            }

            i++;//если не нашли . в строке просто ++ счетчику
        }

        for (int j = 0; j < i; j++) { //обработка строк, если первые два и последние два явлаются модификатором, вывести соотвествующие сообщение
            if (strings[j].charAt(0) == '@'
                    && strings[j].charAt(1) == '@'
                    && strings[j].charAt(strings[j].length() - 1) == '@'
                    && strings[j].charAt(strings[j].length() - 2) == '@') {
                System.out.println("ошибка");
            } else if (strings[j].charAt(0) == '!'
                    && strings[j].charAt(1) == '!'
                    && strings[j].charAt(strings[j].length() - 1) == '!'
                    && strings[j].charAt(strings[j].length() - 2) == '!') {
                System.out.println("предупреждение");
            } else if (strings[j].charAt(0) == '/'
                    && strings[j].charAt(1) == '/'
                    && strings[j].charAt(strings[j].length() - 1) == '/'
                    && strings[j].charAt(strings[j].length() - 2) == '/') {
                System.out.println("информация");
            } else if (strings[j].charAt(0) == '*'
                    && strings[j].charAt(1) == '*'
                    && strings[j].charAt(strings[j].length() - 1) == '*'
                    && strings[j].charAt(strings[j].length() - 2) == '*') {
                System.out.println("подробное сообщение");
            }
        }
    }
}

