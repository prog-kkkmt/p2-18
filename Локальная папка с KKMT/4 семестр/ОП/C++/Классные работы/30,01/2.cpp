#include <iostream>
#include <iomanip>
#include <math.h>
#include <locale>
 using namespace std;
 
int main()
{
	setlocale(0,"");
	int a,b,c,x,y,Z;
	while (true)
	{
		cout << "\n¬ведите X и Y\n";
		cin >> x >> y;
			a=x+y; b=x-y; c=x*y;
			cout << "A = " << a <<endl << "B = " << b << endl<< "C = " << c << endl;  
			Z = a;
		if (b > Z) {Z = b;}
		if (c > Z) {Z = c;}
		cout << "Z= " << Z;
	}
}
