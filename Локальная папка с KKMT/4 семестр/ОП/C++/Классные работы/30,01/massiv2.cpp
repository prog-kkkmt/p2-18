#include <iostream>
#include <iomanip>
#include <ostream>
#include <math.h>
#include <locale>

using namespace std;


int main() 
{
	setlocale(0,"");
	double array[5][5];
	double c[5];
	int Sum=0,temp=0,p=1;
	cout << "Массив 1:" << endl;
    for (int i=0;i<5;i++) 
	{
        for (int j=0;j<5;j++) 
		{
			array[i][j] = 4*sin(7.1*i+j);
            cout << setprecision(3) << setw(9) << array[i][j];
        }
        cout<<endl;
    }
    cout<<endl;
    for (int i=0;i<5;i++) 
	{
		c[i]=1;
        for (int j=0;j<5;j++) 
		{
			c[i]*=array[i][j];
		}
		cout << setw(9) << c[i];
	}
    
}
