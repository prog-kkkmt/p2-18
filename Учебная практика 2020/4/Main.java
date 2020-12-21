package com.company;
//Выполнил Безбородов П2-18

//Задание 4. http://ptaskbook.com/ru/tasks/text.php
//Text44. Дан текстовый файл, каждая строка которого изображает целое число, дополненное слева и справа
//несколькими пробелами. Вывести количество этих чисел и их сумму.


import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
		Path path = Paths.get("in.txt");//название файла в папке с проектом 
		try {
			Scanner scanner = new Scanner(path);//создание сканнера
			int counter = 0;//кол-во чисел
			int sum = 0;//сумма
			while (scanner.hasNextInt()){//пока есть числа в файле
				counter++;//считать кол-во чисел в файле
				sum += scanner.nextInt();//прибавлять число к сумме
			}
			
			System.out.println("Кол-во чисел: " + counter);
			System.out.println("Сумма чичел: " + sum);
		} catch (IOException e) {
			e.printStackTrace();//Вывод ошибки
		}
    }
}
