package com.company;
//Выполнил Безбородов П2-18

//Задание 3. http://ptaskbook.com/ru/tasks/text.php
//Text20. Дан текстовый файл. Заменить в нем все подряд идущие пробелы на один пробел.

import java.io.FileWriter;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Path path = Paths.get("in.txt");//название входного файла в папке с проектом

        try(FileWriter writer = new FileWriter("out.txt", false)){//открыть файл, дать права дописывать в файл(может вызвать ошибку если файл не открыт)
            Scanner scanner = new Scanner(path);//создать сканнер для работы с файлом
            while(scanner.hasNextLine()){//пока есть строки в файле
                String tmp = scanner.nextLine();//считать строку

                while(tmp.contains("  ")){//пока есть два пробела в строке
                    tmp = tmp.replace("  ", " ");//менять два пробела на один
                }

                writer.write(tmp + "\n");//записать в новый файл обработанную строку
            }
        }catch (Exception e){//если файл не открылся(не создался)
            System.out.println(e);//вывод ошибки в консоль
        }
    }
}
