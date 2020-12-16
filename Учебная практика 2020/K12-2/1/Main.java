package com.company;
//Выполнил Безбородов П2-18

import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

//Задание 1. https://stepik.org/lesson/3380/step/3?unit=963
//Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
//Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
//Попробуем написать подобную систему.
//На вход программе первой строкой передаётся количество d известных нам слов, после чего
//на d строках указываются эти слова.
//Затем передаётся количество l строк текста для проверки, после чего l строк текста.
//Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.
//
//Sample Input:
//4
//champions
//we
//are
//Stepik
//3
//We are the champignons
//We Are The Champions
//Stepic
//
//Sample Output:
//stepic
//champignons
//the
public class Main {

    public static void main(String[] args) {
	Scanner scanner = new Scanner(System.in);//input scanner

		//input 1
	int n = Integer.parseInt(scanner.nextLine());
	String[] inputRight = new String[n];
	for(int i = 0; i < n; i++){
	    inputRight[i] = scanner.nextLine();
    }

		//input 2
	int b = Integer.parseInt(scanner.nextLine());
	String[] input = new String[b];

	for(int i = 0; i < b; i++){
	    input[i] = scanner.nextLine();
    }

		Set<String> rightWords = new HashSet<>(Arrays.asList(inputRight)); //Уникальные правильные слова
		Set<String> errors = new HashSet<>(); //уникальные ошибки

        for (int i = 0; i < b; i++){
			scanner = new Scanner(input[i]);

			while(scanner.hasNext()){
				String word = scanner.next();
				for (String rightWord : rightWords) {
					//Если слово не совпадает то добавить в ошибки
					if(!word.equalsIgnoreCase(rightWord)){
						errors.add(word.toLowerCase());
					}
					//Если совпало удалить из ошибок, и перейти к следующему слову
					else{
						errors.remove(word.toLowerCase());
						break;
					}
				}
			}
		}
        
        //Вывод ошибок
		for (String error : errors) {
			System.out.println(error);
		}

    }
}
