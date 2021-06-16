#include <iostream>
#include <fstream>
#include <math.h>
#include <iomanip>

using namespace std;

int main()
{
		fstream xls;
		xls.open("massiv.xls",ios::out);
	double a,b;
	double array[5][5];
	int i,j,sum=0,pr=0;
		for(i=0;i<5;i++)
			{
			for(j=0;j<5;j++)
				{
					array[i][j]=7*sin(2.3*i*j);
				 	xls << "\t" << setprecision(3) <<array[i][j];
				}
				xls << endl;
			}
			xls.close();
			
}

