package myPack;

public class Student extends Human{
    private int course;//поля класса

    public Student(int age, String name, int course) {//конструктор
        super(age, name);
        this.course = course;
    }

    public int getCourse() {//геттер для курса
        return course;
    }

    public void showInfo(){//вывод информации
        System.out.println("age:" + getAge() + " name: " + getName() + " course: " + getCourse() + " " + this.getClass());
    }
}
