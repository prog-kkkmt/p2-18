package com.company;
//Выполни Безбородов П2-18

//Задание 1. http://ptaskbook.com/ru/tasks/text.php
//Text5. Дана строка S и текстовый файл. Добавить строку S в конец файла.

import java.io.FileWriter;
import java.util.Scanner;
import java.util.concurrent.ExecutionException;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();//чтение строки
        try(FileWriter writer = new FileWriter("out.txt", true)){//открыть файл, дать права дописывать в файл
            writer.write(input);//Дописать в файл
        }catch (Exception e){//если файл не открылся(не создался)
            System.out.println(e);//вывод ошибки
        }

    }
}
