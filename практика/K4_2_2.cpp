/*
������� 2. ����������� ��������� � ���� ��� ������������ ������ � ������ ������:
������(list), �������(dict), ���������(set)
���� -> ����� ���� ������ -> ����� ������ -> ������� �������
*/
#include <iostream>
#include <fstream>
#include <string>
int menu()
{
    std::cout << "1. ������ ��� ������" << std::endl;
    std::cout << "2. ������ ��� ���������" << std::endl;
    std::cout << "3. ������ ��� �������" << std::endl;
    std::cout << "0. ����� �� ���������" << std::endl;
    std::cout << "�������� ����� ����: " <<std::endl;
}
int main()
{
    setlocale(LC_ALL, "Russian");
	std::ifstream fin("file.txt");
	char buff[50];
	int choise;
	std::string stringLine = "";
    int lineNumber = 0;
	if (!fin.is_open())
		std::cout << "Error" << std::endl;
	else
	{
        menu();
        std::cin >> choise;
        switch (choise)
        {
        case 1:
            for (int i = 0; i < choise; i++)
                fin.getline(buff, 50);
            std::cout << buff;
            break;
        case 2:
            for (int i = 0; i < choise; i++)
                fin.getline(buff, 50);
            std::cout << buff;
            break;
        case 3:
            for (int i = 0; i < choise; i++)
                fin.getline(buff, 50);
            std::cout << buff;
            break;
        case 0:
            return 0;
            break;
        default:
            break;
        }
	}
}
