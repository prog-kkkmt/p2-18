// Дано вещественное число — цена 1 кг конфет. Вывести стоимость 1, 2, …, 10 кг конфет.

#include <iostream>
#include <time.h>
#include <stdlib.h>

using namespace std;

int main()
{
int value;
cout << "value = "; 
cin >> value;
for (int i = 1; i <= 10; i ++){
	cout << value * i << endl;
	
}
return 0; // возвращаем 0
}
