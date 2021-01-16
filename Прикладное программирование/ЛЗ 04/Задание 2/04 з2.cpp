/*���������: ��������� �.�., �������� �.�., �������� �.�.
  ������: ���� �2-18
  �������: ����������� ��������� � ���� ��� ������ � �������� ����� ����� �� 10 ���������.
������ ����: ����������, ���������� �������������, ���������� �����, ������, �����.
��� ������� �������� (����� ������) ����������� �������, ����������� � �������� ���������� 
����� ������� �������� ������� � ���������� ���������*/

#include <iostream>	

using namespace std;

int Filling(int array[], int size){
	system("cls");
    for (int i = 0; i < size; i++){
    	cout << ">";
        cin >> array[i];
    }
}

int Max(int array[], int size){
	system("cls");
	int i = 0;
    int Max = array[i];
    for (i = 1; i < size; i++){
        if (array[i] > Max)
            Max = array[i];
	}
    return Max;
}

int Sum(int array[], int size){
	system("cls");
	int sum = 0;
    for (int i = 0; i < size; i++){
        sum = sum + array[i];
    }
    return sum;
}

int Printing(int array[], int size){
	system("cls");
	for (int i = 0; i < size; i++){
        cout << array[i] << " ";
    }
}

int main(){
	int size, array[size], number = 1;
	cout << "Enter the number of elements of the array\n" << "\n>>>";
	cin >> size;
	while(number != 0){
		cout << "\n1. Filling\n" << "2. Max\n" << "3. Sum\n" << "4. Printing\n" << "0. Exit\n" << "\n>>>";
		cin >> number;
		switch(number){
			case 1: Filling(array, size); break;
			case 2: cout << "Max: " << Max(array, size) << endl; break;
			case 3: cout << "Sum: " << Sum(array, size) << endl; break;
			case 4: cout << "Printing: " << Printing(array, size) << endl; break;
			case 0: return EXIT_SUCCESS; break;
			default: 
				cout << "\nIncorrect number entered"; break;
		}
	}
	return 0;
}
