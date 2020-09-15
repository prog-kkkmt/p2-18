package MyFirstPack;

/*
* Sample Input 1:
*   18 35
*Sample Output 1:
*   1
*/


import java.util.Scanner;

class Meta {
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
        System.out.println(Meta.NOD(a,b));//вывод
    }
}
