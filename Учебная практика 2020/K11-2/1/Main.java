package com.company;
//Выполнил Безбородов П2-18



//Задание 1. https://stepik.org/lesson/243394/step/4?unit=215740
//Телефонная книга. Этап 1. Коля устал запоминать телефонные номера и заказал у Вас
//программу, которая заменила бы ему телефонную книгу. Коля может послать программе
//два вида запросов: строку, содержащую имя контакта и его номер, разделенные пробелом,
//или просто имя контакта. В первом случае программа должна добавить в книгу новый номер,
//во втором – вывести номер контакта. Ввод происходит до символа точки. Если введенное
//имя уже содержится в списке контактов, необходимо перезаписать номер.
//
//Sample Input:
//Ben 89001234050
//Alice 210-220
//Alice
//Alice 404-502
//Nick +16507811251
//Ben
//Alex +4(908)273-22-42
//Alice
//Nick
//Robert 51234047129
//Alex
//.
//
//Sample Output:
//210-220
//89001234050
//404-502
//+16507811251
//+4(908)273-22-42

import java.util.ArrayList;
import java.util.Scanner;

//структура контакта
class TelephoneContact{
    String contactName;
    String number;
//констуктор для контакта
    TelephoneContact(String contactName, String number){
        this.contactName = contactName;
        this.number = number;
    }
}


public class Main {

    public static void main(String[] args) {
        //Структура данных  для контактов
        ArrayList<TelephoneContact> telephoneBook = new ArrayList<>();


        String find = null;
        int k = 0;

        Scanner scanner = new Scanner(System.in);
        String testString = new String("null");//строка для проверки конца ввода
        String[] input = new String[100];

        while (true) {
            testString = scanner.nextLine();//читает строку с консоли если . прекращает whille
            if (testString.contains(".")) {
                break;
            } else {//если не точка то продолжает читать строки и записывать в массив входных данных
                input[k] = testString;
            }
            k++;
        }
        //обработка входных данных
        for (int j = 0; j < k; j++) {
            boolean found = false;
            Scanner inputWorker = new Scanner(input[j]);

            if (input[j].contains(" ")) {// если содержит два слова в строке значит нужно выполнить поиск
                find = inputWorker.next();
                //поиск контакта
                for (int i = 0; i < telephoneBook.size(); i++) {
                    if (find.equals(telephoneBook.get(i).contactName)) {//если находит found = true
                        telephoneBook.get(i).number = inputWorker.next();//меняет номер
                        found = true;
                        break;
                    }
                }

                if (!found) {//если нашло то уже изменило, и этот блок не выполняется
                    //Добавление нового контакта//если не нашло то добавляет в книгу новый контакт
                    telephoneBook.add(new TelephoneContact(find, inputWorker.next()));
                }

            } else {
                //logic to show contact
                // если во входных данных нет пробела, надо вывести номер контакта
                find = inputWorker.next();

                for (int i = 0; i < telephoneBook.size(); i++) {
                    //находит контакт и выводит номер
                    if (find.equals(telephoneBook.get(i).contactName)) {
                        System.out.println(telephoneBook.get(i).number);
                        break;
                    }
                }
            }
        }

    }
}
