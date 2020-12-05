package com.company;

public class Human {
    private String name;
    private int age;

    Human(int age, String name){
        this.age = age;
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public String getName() {
        return name;
    }

    public void showInfo(){
        System.out.println("Человек: %s, в возрасте: %d, this.name, this.age");
    }
}
