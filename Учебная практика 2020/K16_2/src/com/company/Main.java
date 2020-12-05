package com.company;

//Задание 1. Создание классов
//Задание 2. Создание экземпляров класса
//Задание 3. Доступ к атрибутам
//Задание 4. Встроенные атрибуты класса
//адание 5. Уничтожение объектов (сбор мусора)



public class Main {

    public static void main(String[] args) {
	Student student = new Student(19, "Konstantin", 3);// создание объекта моего класса
	System.out.format("Студент: %s, в возрасте: %d, учится на %d курсе", student.getName(), student.getAge(), student.getCourse());//вывод данных объекта через геттеры
    }
}
