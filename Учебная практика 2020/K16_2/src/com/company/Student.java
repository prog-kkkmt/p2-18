package com.company;

public class Student{
    private int age;//поля/атрибуты
    private String name;
    private int course;

    Student(int age, String name, int course){//конструктор
        this.age = age;
        this.name = name;
        this.course = course;
    }

    public String getName() {//геттеры
        return name;
    }

    public int getAge() {
        return age;
    }

    public int getCourse() {
        return course;
    }
}
