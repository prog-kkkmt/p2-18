package com.company;

/*
 * С использованием результата задания 2 разработать программу для нахождения наименьшего
общего кратного
 */


import java.util.Scanner;

class Worker {
    public static int NOD(int a, int b){
        while(true){ //метод евклида

            if ( a == 0){
                return b;
            }

            else if (b == 0){
                return a;
            }

            else if(a >= b){
                a = a % b;
            }

            else if(b >= a){
                b = b % a;
            }
        }
    }
}


public class Main
{
    public static void main(String[] args) {
        Scanner scaner = new Scanner(System.in);//ввод
        int a = scaner.nextInt();
        int b = scaner.nextInt();

        int nok = a * b /  Worker.NOD(a,b); // nok = a * b / наиб общ делит
        System.out.println(nok);
    }


}
