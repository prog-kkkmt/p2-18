/*Выполнили: Короленко И.Р., Кузнецов М.С., Слесарев А.М.
  Группа: ККМТ П2-18
*/

#include <iostream>	

using namespace std;	

void rotate(int a[], unsigned size, int shift){	
    while(shift != 0){	
        int temp = a[0];	
        for(int i=1; i < size; i++){	
            a[i-1] = a[i];
		}	
        a[size-1] = temp;
		shift--;
	}	
}	

int main (){	
	int size, shift;	
	cout << "Input [size] i [shift]" << endl;	
	cin >> size >> shift;	
	int a[size];	
	for (int i = 0; i < size; i++)	
		cin >> a[i];	
		rotate (a,size, shift);	
	for (int i = 0; i < size; i++)	
		cout << a[i];	
	return 0;
}
