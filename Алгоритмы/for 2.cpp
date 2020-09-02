/*Выполняли Щепкин и Бурлаев*/

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

