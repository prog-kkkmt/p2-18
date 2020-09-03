//Proc1. ќписать процедуру PowerA3(A, B), вычисл€ющую третью степень числа
//A и возвращающую ее в переменной B (A Ч входной, B Ч выходной параметр;
//оба параметра €вл€ютс€ вещественными). — помощью этой процедуры найти третьи степени п€ти данных чисел.



#include <iostream>
#include <math.h>

using namespace std;



float powerA3(float a){ //процедура возведени€ числа в 3 степень
    float answer = 0;
    answer = pow(a,3);
    return answer;
}

int main()
{

	float a[5]; // входные данные

	for(int i = 0; i < 5; ++i){
    		cin >> a[i];
    	}

	cout << "answers: \n";

	for(int i  = 0; i < 5; ++i){ // вывод
    	cout << powerA3(a[i])<< "\n";
}

return 0;
}
