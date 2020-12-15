package com.company;
//Выполнил Безбородов П2-18



//Задание 3. https://stepik.org/lesson/243394/step/13?unit=215740
//Телефонная книга. Этап 3. Коле очень понравилась Ваша программа, однако он стал
//замечать, что иногда в его телефонную книгу попадают номера в некорректном формате.
//Чтобы не сохранять недействительные номера, он попросил Вас обрабатывать только номера,
//соответствующие критериям:
//- номер должен начинаться либо с +7, либо с 8 и состоять из 11 цифр.
//- блоки цифр могут разделяться пробелами или дефисами.
//- вторая, третья и четвертая цифры могут помещаться в скобки.
//Если программа встречает некорректный номер, она должна его проигнорировать. В обратном
//случае она должна привести номер к виду +7 (900) 800-70-60 и запомнить. Остальной
//функционал программы остается без изменений.
//
//Sample Input:
//Ben 89001234050, +7 050 432 10-09,
//Alice 894053212-65,
//Nick +1(650)781 12-51,
//Ben
//Alex 8 (908) 273-22-42,
//Alice
//Nick
//Robert 89174043215,
//Alex
//Robert
//.
//
//Sample Output:
//+7 (900) 123-40-50, +7 (050) 432-10-09
//+7 (940) 532-12-65
//Не найдено
//+7 (908) 273-22-42
//+7 (917) 404-32-15

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.Scanner;


class Worker{
    public static String toCorrectNumber(String a){
        StringBuilder sb =  new StringBuilder();
        StringBuilder out = new StringBuilder();
        for(int i = 0; i < a.length(); i++) {
            if (Character.isDigit(a.charAt(i))){//преобразовать строку произвольного номер в номер типа 00000000000
                sb.append(a.charAt(i));
            }
        }
        if(sb.length() != 11){//если номер не из 11 чисел ошибка, и вернут "-"(использую как код ошибки)
            return "-";
        }else if(sb.charAt(0) != '+' && sb.charAt(0) != '7' && sb.charAt(0) != '8'){//если номер начинается не с валидных символов вернуть ошибку
            return "-";
        }
        else{
            out.append("+7 (");//если все правильно разбить номер на формат +7 (000) 777-00-00
            for(int i = 4, j = 1;i < 18;i++,j++){
                if(i == 7){
                    out.append(")");
                    j--;
                }else if(i == 8){
                    j--;
                    out.append(" ");
                }else if(i == 12){
                    j--;
                    out.append("-");
                }else if(i == 15){
                    j--;
                    out.append("-");
                }else {
                    out.append(sb.charAt(j));
                }
            }
        }
        //вернуть результат
        a = String.valueOf(out);
        return a;
    }
}


//структура контакта
class TelephoneContact{
    String contactName;
    Queue<String> numbers = new ArrayDeque<>();//очередь для вывода в порядке добавления

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
        boolean printed = false;
        StringBuilder helper = new StringBuilder();

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
                        helper.append(workScanner.next());
                        if(helper.charAt(helper.length()-1) ==',') {
                            telephoneBook.get(telephoneBook.size() - 1).addNumber(Worker.toCorrectNumber(String.valueOf(helper)));//записать номера в последний добавленный контакт
                            helper = new StringBuilder();
                        }
                    }
                }
            }
            //show contact
            else{
                for (TelephoneContact telephoneContact : telephoneBook) {
                    printed = false;
                    if (telephoneContact.contactName.equals(name)) {

                        for (String number : telephoneContact.numbers) {
                            if (number.equals("-")){
                                System.out.println("Не найдено");
                                printed = true;
                            }else {
                                System.out.print(number + ", ");
                            }

                        }
                        if(!printed) {
                            System.out.println("");
                        }
                    }
                }
            }
        }
    }
}
