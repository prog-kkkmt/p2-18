#include <iostream>
using namespace std;

void rotate(int a[], unsigned size, int shift){
    while(shift!=0){
        int temp=a[0];
        for(int i=1;i < size;i++){
            a[i-1]=a[i];}
            a[size-1]=temp;shift--;}
return;
}

int main ()
{
	int size, shift;
	cout << "Vvedite size i shift" << endl;
	cin >> size >> shift;
	int a[size];
	for (int i = 0 ; i < size ; i++)
		cin >> a[i];
	rotate (a,size, shift);
	for (int i = 0 ; i < size ; i++)
		cout << a[i];
	
}
