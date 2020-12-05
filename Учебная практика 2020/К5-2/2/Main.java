package com.company;
import java.util.Scanner;

//Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу
//в строке, и после первого введенного нуля выводит сумму полученных на вход чисел.
//Sample Input 1:
//5
//-3
//8
//4
//0
//Sample Output 1:
//14
//
//Sample Input 2:
//0
//Sample Output 2:
//0

public class Main {

    public static void main(String[] args) {
        int answer = 0;//поле ответа
        int prev = answer;// для отслеживания 0
        boolean run = true;//переменная для цикла

        Scanner scanner = new Scanner(System.in);//ввод

        while (run){
            answer += scanner.nextInt();//считать  число и прибавить к ответу
            if(prev == answer){// если число не изменилось значит мы считали 0, следующей итерации не будет
                run = false;
            }
            prev = answer;//если число изменилось, то изменить переменную на результат сложения, и выполнить цикл еще раз
        }

        System.out.println(answer);//вывод
    }
}