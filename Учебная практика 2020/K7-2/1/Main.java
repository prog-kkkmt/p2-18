package com.company;
//Задание 1. Подготовить сравнительную инструкцию по использованию
//форматирования строк

public class Main {

    public static void main(String[] args) {
        int age = 19;
        String name = "Kostya";

        String output = String.format("%s is %d years old.", name, age);//форматный вывод

        System.out.println(output);
    }
}
