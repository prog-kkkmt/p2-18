/* Описать процедуру Inv(A, N), меняющую порядок следования элементов вещественного массива A размера N на обратный (инвертирование массива). Массив A является входным и выходным параметром.
 С помощью этой процедуры инвертировать массивы A, B, C размера NA, NB, NC соответственно.*/
#include <iostream>
#include <time.h>
#include <stdlib.h>

using namespace std;

int* inv(int A[], const int N)
{

for (int i = 0; i < N/2 ; i++)
	swap(A[i], A[N-i-1]);
	
return A;
}

int main()
{
	srand(time(0));
const int n = 12;
int A[n];
int B[n];
int C[n];

for (int i = 0; i < n; i++)
{
	A[i] = rand()%10-5;
	cout << A[i] << " ";
}
inv(A, n);
cout << endl << endl<< "A: ";

for (int i = 0; i < n; i++)
	cout << A[i] << " ";

	cout << endl << endl;
for (int i = 0; i < n; i++)
{
	B[i] = rand()%10-5;
	cout << B[i] << " ";
}
inv(B, n);
cout << endl << endl << "B: ";

for (int i = 0; i < n; i++)
	cout << B[i] << " ";
	
	cout << endl << endl;
for (int i = 0; i < n; i++)
{
	C[i] = rand()%10-5;
	cout << C[i] << " ";
}

inv(C, n);

cout << endl << endl << "C: ";

for (int i = 0; i < n; i++)
	cout << C[i] << " ";
	

return 0; // возвращаем 0
}
