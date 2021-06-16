#include <iostream>
#include <iomanip>
#include <math.h>
#include <locale>
 using namespace std;
 
int main()
{
	setlocale(0,"");
	 int x,Z;
	cout << "¬ведите число Z\n>";
		cin >> x;
		if (0<=x && x<=5) {Z = abs(x);} 
		else if (x<0) {Z = pow(x,2);} 
		else Z = 5; cout << "Z=" << Z;
	return 0; 
}
