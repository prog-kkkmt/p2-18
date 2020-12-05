package myPack;

public class Worker extends Human {//поля класса
    int payday;

    public Worker(int age, String name, int payday) {//конструктор
        super(age, name);
        this.payday = payday;
    }

    public int getPayday() {//геттер
        return payday;
    }

    public void showInfo() {// получени информации объекта
        System.out.println("age:" + getAge() + " name: " + getName() + " payday: " + getPayday() + " " + this.getClass());
    }
}
