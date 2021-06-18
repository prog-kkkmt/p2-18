#include <iostream>
#include <vector>
class EventObserver
{
public:
	virtual void Handle(int num) = 0;
};
class Event
{
public:
	std::vector<EventObserver*> observer;
	void notify(int num)
	{
		for (EventObserver* o : observer)
		{
			o->Handle(num);
		}
	}
};
class Menu
{
protected:
	int num, num2;
public:
	Event sum;
	Event fib;
	int count;
	void setSum(int value)
	{
		num = value;
		if (num > 0)
		{
			sum.notify(num);
		}
		else
		{
			std::cout << "Error" << std::endl;
		}
	}
	int getSum()
	{
		count = num;
		return num;
	}
	void giveFib(int value)
	{
		num2 = value;
		fib.notify(num2);
	}
};
class EventSum : public EventObserver //  класс наследующий класс наблюдателя, и выводящий сумму всех чисел в массиве
{
protected:
	int numArray = 0, arrayNum[100];
public:
	void Handle(int num) override
	{
		std::cout << "Enter " << num << " num: " << std::endl;
		for (int i = 0; i < num; i++)
		{
			std::cin >> arrayNum[i];
		}
		for (int i = 0; i < num; i++)
		{
			numArray += arrayNum[i];
		}
		std::cout << "Sum: " << numArray << std::endl;
	}
};
class EventFib : public EventObserver //  класс наследующий класс наблюдателя, и выводящий числа фибоначчи
{
protected:
	int arrayNum[100];
public:
	void Handle(int num) override
	{
		std::cout << "Enter " << num << " num: " << std::endl;
		arrayNum[0] = 0;
		arrayNum[1] = 1;
		std::cout << arrayNum[0] << "\n" << arrayNum[1] << std::endl;
		for (int i = 0; i < num; i++)
		{
			if (i >= 1)
			{
				arrayNum[i + 1] = arrayNum[i - 1] + arrayNum[i];
				std::cout << "Sum: " << arrayNum[i + 1] << std::endl;
			}
		}
	}
};

int main()
{
	int num = 0, option = 0;
	bool isOpen = true;
	Menu choise;
	std::cout << "Enter count num: " << std::endl;
	std::cin >> num;
	choise.sum.observer.push_back(new EventSum());
	choise.fib.observer.push_back(new EventFib());
	while (isOpen)
	{
		std::cout << std::endl;
		std::cout << "/////////////////" << std::endl;
		std::cout << "Enter operation: " << std::endl;
		std::cout << "//1. sum         " << std::endl;
		std::cout << "//2. fib         " << std::endl;
		std::cout << "//3. exit         " << std::endl;
		std::cout << std::endl;
		std::cin >> option;
		switch (option)
		{
		case 1:
			choise.setSum(num);
			break;
		case 2:
			choise.giveFib(num);
			break;
		case 3:
			isOpen = false;
			break;
		default:
			break;
		}
	}
	return 0;
}
