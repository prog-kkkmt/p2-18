package com.company;
//Выполнил Безбородов П2-18

//Задание 4. https://pythontutor.ru/lessons/sets/problems/number_of_words/
//Задача «Количество слов в тексте»
//Условие. Дан текст: в первой строке записано число строк, далее идут сами строки.
//Определите, сколько различных слов содержится в этом тексте.
//Словом считается последовательность непробельных символов идущих подряд, слова разделены
//одним или большим числом пробелов или символами конца строки.


import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {

    public static void main(String[] args) {
	int n = 100;//default var
	Set<String> set = new HashSet<>();//сет для хранения уникальных слов текста

	Scanner scanner = new Scanner(System.in);
	n = Integer.parseInt(scanner.nextLine());//считать кол-во строк
	String[] input = new String[n];//создать массив строк 
	for(int i = 0; i < n;i++){
		input[i] = scanner.nextLine();//считать строки
	}
	for(int i = 0;i < n;i++){
		scanner = new Scanner(input[i]);
			while(scanner.hasNext()) {
				set.add(scanner.next());//добавлять в сет слова из текста, при совпадении слово не будет добавленно
			}
		}
	System.out.println(set.size());//вывод кол-во уникальных слов в тексте
    }
}
