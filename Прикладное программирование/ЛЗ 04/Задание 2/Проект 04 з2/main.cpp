/*���������: ��������� �.�., �������� �.�., �������� �.�.
  ������: ���� �2-18
  �������: ����������� ��������� � ���� ��� ������ � �������� ����� ����� �� 10 ���������.
������ ����: ����������, ���������� �������������, ���������� �����, ������, �����.
��� ������� �������� (����� ������) ����������� �������, ����������� � �������� ����������
����� ������� �������� ������� � ���������� ���������*/

#include "functions.h"

using namespace std;

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
