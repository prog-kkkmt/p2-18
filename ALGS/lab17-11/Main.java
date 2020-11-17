package com.company;

//работает для одного магазина
//подключение готовых джава классов
import java.io.*;
import java.util.Scanner;
import java.util.Stack;

class Ammo{ // структура одного патрона
    private int id; //номер
    private float c; //калибр

    Ammo(int id, float c){//констуктор для патрона
        this.id = id;
        this.c = c;
    }

    //геттеры для переменных патрона
    public int getId() {
        return id;
    }

    public float getC() {
        return c;
    }
}

    //структура магазина
class Magazin{
    private float minCalibr; //минимальный калибр для магазина
    private float maxCalibr; //максимальный калибр в магазине
    private int capatity; //вместимость магазина

    Magazin(int capatity, float minCalibr, float maxCalibr){//конструктор для магазина
        this.capatity = capatity;
        this.minCalibr = minCalibr;
        this.maxCalibr = maxCalibr;
    }

        //геттеры для переменных магазина
    public int getCapatity() {
        return capatity;
    }

    public float getMaxCalibr() {
        return maxCalibr;
    }

    public float getMinCalibr() {
        return minCalibr;
    }
}

public class Main {

    public static void main(String[] args) {
        //пути к файлам
        File file = new File("D:\\laba\\src\\com\\company\\input.txt");//входные данные
        File magazineFile = new File("D:\\laba\\src\\com\\company\\magazine.txt"); //данные обоймы
        File fileWritterGilzaPath = new File("D:\\laba\\src\\com\\company\\gilza.txt"); //патроны которые влезли в обойму
        File fileWrittterBox2Path = new File("D:\\laba\\src\\com\\company\\box2.txt"); //патроны которые не влезли в обойму
        File fileWrittterViborPath = new File("D:\\laba\\src\\com\\company\\vibor.txt"); // макс и мин

        try {
            float max;//переменная для макс
            float min;//переменная для мин
            Scanner magazineScanner = new Scanner(magazineFile);//сканнер для работы с данными магазина
           Scanner scan = new Scanner(file);//сканнер для работы с входными данными
           Stack<Ammo> stack = new Stack<>();//стек для хранения патронов которые влезли

            //создание объекта магазина с данными файла
           Magazin mag = new Magazin(magazineScanner.nextInt(), magazineScanner.nextFloat(), magazineScanner.nextFloat());

           //создание файлВрайтеров
            PrintWriter fileWriter = new PrintWriter(fileWritterGilzaPath);//попали
            PrintWriter fileWriter1 = new PrintWriter(fileWrittterBox2Path);//не попали
            PrintWriter fileWriter2 = new PrintWriter(fileWrittterViborPath);//выбор



           int capatity = scan.nextInt();//считать количество патронов во входных данных
            Ammo ammo; // создать ссылку для патрона
                   for(int i = 0;i<capatity;i++){//пока не переберет все патроны
                       ammo = new Ammo(scan.nextInt(),scan.nextFloat()); //создавать патрон исходя из входных данных
                       if(stack.size() != mag.getCapatity()) {//пока маназин не переполнен
                           if (ammo.getC() >= mag.getMinCalibr() && ammo.getC() <= mag.getMaxCalibr()) { //если патрон влезает
                               stack.add(ammo);//добавить в стек
                           }else {//если патрон не влазиет записать в бокс2
                               fileWriter1.write(String.valueOf(ammo.getId()) + " " + String.valueOf(ammo.getC())  + " ");
                           }
                       }else if(stack.size() == mag.getCapatity()){//если магазин переполнен записывать все данные сразу в бокс2 без проверки осталось ли место в магазине
                           fileWriter1.write(String.valueOf(ammo.getId()) + " " + String.valueOf(ammo.getC())  + " ");
                       }
                   }
                   //присвоить макс и мин верхнему элементу стека
                    max = stack.peek().getC();
                    min = stack.peek().getC();
                    //пока стек не пуст
                   while (!stack.isEmpty()){
                       fileWriter.write(String.valueOf(stack.peek().getId()) + " " + String.valueOf(stack.peek().getC())  + " ");//записывать в гильзу
                        //находить макс и мин
                       if(stack.peek().getC() > max){
                           max = stack.peek().getC();
                       }else if(stack.peek().getC() < min){
                           min = stack.peek().getC();
                       }

                       stack.pop();// крайний удалять элемент стека
                   }
                   fileWriter2.println("max vivor = " + max + "\nmin vibor = " + min);//записать макс и мин в выбор

                    //закрыть файлы
                    fileWriter.close();
                    fileWriter1.close();
                    fileWriter2.close();

        //обработка исключения если файл не найден, в данном случае просто выводит ошибку в консоль
        }catch (FileNotFoundException e) {
            System.out.println(e);
        }
    }
}
