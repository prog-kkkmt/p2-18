#include <iostream>
#include <iomanip>
#include <ostream>
#include <locale>

using namespace std;


int main() 
{
	setlocale(0,"");
	int array[6][8];
	int Sum=0,temp=0,p=1;
	cout << "Массив 1:" << endl;
    for (int i=0;i<6;i++) 
	{
        for (int j=0;j<8;j++) 
		{
			array[i][j] = 3*i - 5*j;
            cout << setw(6) << array[i][j];
        }
        cout<<endl;
    }
    
    for(int j=0;j<8;j++)
    {
    	Sum += array[1][j];
    }
    cout << "S=" << Sum << endl;
    
    for(int j=0;j<8;j++)
    {
    	temp=array[0][j];
    	array[0][j]=array[2][j];
    	array[2][j]=temp;
    }
    
    for(int i=0;i<6;i++)
	{
		for(int j=0;j<8;j++)
		{
			cout << setw(6) << array[i][j];
		}
		cout<<endl;
    }
    
    for(int i=0;i<=2;i=i+1)
    {
    	p=p*(array[i][1]-array[i][0]);
    }
    cout << "P=" << p << endl;
    
}
