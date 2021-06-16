#include <iostream>
#include <math.h>
#include <locale>
#include <cmath>
#include <cstdlib>
#include <string>
#include "function.cpp"
#include "w1.cpp"

using namespace std;

int main()
{
	system("title Menu by (ivauuka99)");
	setlocale(0, "");
	int key;
	while (1)
	{
		system("cls");
		cout << "|Выберите соответствующий пунк задания:|" << endl;
		cout << "========================================" << endl;
		cout << "|1 |            Задание №1             |" << endl;
		cout << "|2 |            Задание №2             |" << endl;
		cout << "|3 |            Задание №3             |" << endl;
		cout << "|4 |            Задание №4             |" << endl;
		cout << "|5 |            Задание №5             |" << endl;
		cout << "|6 |            Задание №6             |" << endl;
		cout << "|7 |            Задание №7             |" << endl;
		cout << "|8 |            Задание №8             |" << endl;
		cout << "|9 |            Задание №9             |" << endl;
		cout << "|10|            Задание №10            |" << endl;
		cout << "|0 |              Выход                |" << endl;
		cout << "========================================" << endl;
		cin >> key;
		switch (key)
		{
		case '1': w1(); break;
		default: "Ошибка ввода";
		}
	}

}