/*For2. Даны два целых числа A и B (A < B). Вывести в порядке возрастания все целые числа, 
расположенные между A и B (включая сами числа A и B), а также количество N этих чисел.*/
#include <stdio.h>
#include <iostream>

using namespace std;

int main ()

{
	int a,b,n=0,i;
	cin >> a >> b; 
	while (a<=b)
	{
	
	cout << a++;
	cout <<"-";
	n++;
	
	}
	cout<< "(" << n << ")";
	return 0;
	
	
	
}

