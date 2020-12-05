package com.company;


//Задание 1. Придумать собственный класс
//Задание 2. Неформально описать функционал класса
//Задание 3. Реализовать класс в модуле
//Задание 4. Разработать скрипт для демонстрации работы с классом (импортировать модуль,
//создать экземпляры, вызвать методы)

import myPack.*;

public class Main {

    public static void main(String[] args) {
        Student studentOb = new Student(19, "kostya", 3);//создание объектов
        Human humanOb = new Human(23, "Harry");
        Worker workerOb = new Worker(18, "Denis", 2000);

        humanOb.showInfo();//вызов методов для получения информации
        studentOb.showInfo();
        workerOb.showInfo();

    }
}
