package com.company;
//Выполнил Безбородов П2-18



//Задание 2. https://stepik.org/lesson/243394/step/8?unit=215740
//Телефонная книга. Этап 2.     Коля понял, что у многих из его знакомых есть несколько
//телефонных номеров и нельзя хранить только один из них. Он попросил доработать Вашу
//программу так, чтобы можно было добавлять к существующему контакту новый номер или даже
//несколько номеров, которые передаются через запятую. По запросу телефонного номера
//должен выводиться весь список номеров в порядке добавления, номера должны разделяться
//запятой. Если у контакта нет телефонных номеров, должна выводиться строка "Не найдено".
//
//Sample Input:
//Ben 89001234050, +70504321009
//Alice 210-220
//Alice
//Alice 404-502, 894-005, 439-095
//Nick +16507811251
//Ben
//Alex +4(908)273-22-42
//Alice
//Nick
//Robert 51234047129, 92174043215
//Alex
//Robert
//.
//
//Sample Output:
//210-220
//89001234050, +70504321009
//210-220, 404-502, 894-005, 439-095
//+16507811251
//+4(908)273-22-42
//51234047129, 92174043215

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.Scanner;

//структура контакта
class TelephoneContact{
    String contactName;
    Queue<String> numbers = new ArrayDeque<>();

    //констуктор для контакта
    TelephoneContact(String contactName){
        this.contactName = contactName;
    }

    public void addNumber(String number){
        this.numbers.add(number);
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
            testString = scanner.nextLine();//читает строку с консоли если . прекращает while
            if (testString.contains(".")) {
                break;
            } else {//если не точка то продолжает читать строки и записывать в массив входных данных
                input[k] = testString;
            }
            k++;
        }

        //обработка входных данных
        for (int j = 0; j < k; j++) {
            Scanner workScanner = new Scanner(input[j]);
                String name = workScanner.next();
                boolean found = false;

                //find contact
            if(input[j].contains(" ")) {
                for (TelephoneContact telephoneContact : telephoneBook) {
                    if (telephoneContact.contactName.equals(name)) {
                        while (workScanner.hasNext()) {
                            telephoneContact.addNumber(workScanner.next());
                            found = true;
                        }
                    }
                }

                //new contact
                if (!found) {
                    telephoneBook.add(new TelephoneContact(name));//если не нашло создать контакт
                    while (workScanner.hasNext()) {
                        telephoneBook.get(telephoneBook.size() - 1).addNumber(workScanner.next());//записать номера в последний добавленный контакт
                    }
                }
            }
                //show contact
            else{
                for (TelephoneContact telephoneContact : telephoneBook) {
                    if (telephoneContact.contactName.equals(name)) {
                        for (String number : telephoneContact.numbers) {
                            System.out.print(number + " ");
                        }
                        System.out.println("");
                    }
                }
            }
        }
    }
}
