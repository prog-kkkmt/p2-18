package myPack;

public class Human {
    private int age;//поля класса
    private String name;

    public Human(int age, String name){//конструктор
        this.age = age;
        this.name = name;
    }

    public String getName() {//геттеры
        return name;
    }

    public int getAge() {
        return age;
    }

    public void showInfo(){//вывод информации объекта
        System.out.println("age:" + getAge() + " name: " + getName() + " " + this.getClass());
    }
}
