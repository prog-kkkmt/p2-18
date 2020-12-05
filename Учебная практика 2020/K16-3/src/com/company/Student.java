package com.company;

public class Student extends Human{

    private int course;

    Student(int age, String name, int course){//конструктор
        super(age, name);
        this.course = course;
    }

    public int getCourse() {
        return course;
    }

    @Override
    public void showInfo() {
        System.out.format("Студент: %s, в возрасте: %d, учится на %d курсе", this.getName(), this.getAge(), this.getCourse());
    }
}
