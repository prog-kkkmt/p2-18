#include <iostream>
#include <cstdlib>
#include <ctime>
#include <random>
#include <SFML/Graphics.hpp>
using namespace std;
const int wallNoEnter = 0, passEnter = 1;
int A, B, countA, countB, idVolnA, idVolnB;
//////////////////////////////
// Функция определяющая тупики
bool deadend(int x, int y, int** mazeArray, int height, int width)
{
	int a = 0;

	if (x != 1)
	{
		if (mazeArray[y][x - 2] == passEnter)
			a += 1;
	}
	else a += 1;

	if (y != 1)
	{
		if (mazeArray[y - 2][x] == passEnter)
			a += 1;
	}
	else a += 1;

	if (x != width - 2)
	{
		if (mazeArray[y][x + 2] == passEnter)
			a += 1;
	}
	else a += 1;

	if (y != height - 2)
	{
		if (mazeArray[y + 2][x] == passEnter)
			a += 1;
	}
	else
		a += 1;
	if (a == 4)
		return 1;
	else
		return 0;
}
/////////////////////////
// Отображение результата
void visualSFML(int** mazeArray, int height, int width)
{
	sf::RenderWindow window(sf::VideoMode(640, 480), "Labirint");
	sf::Event e;
	sf::RectangleShape rectangle;
	rectangle.setScale(8, 8);
	for (int i = 0; i < A; i += 21)
	{
		idVolnA++;
	}
	for (int i = 0; i < B; i += 21)
	{
		idVolnB++;
	}
	std::cout << idVolnA << " " << idVolnB << std::endl;
	sf::Texture wallTexture;
	sf::Sprite wallSprite;
	wallTexture.loadFromFile("sprites/wall.png");
	wallSprite.setTexture(wallTexture);
	wallSprite.setPosition(15, -300);
	wallSprite.setScale(0.7, 0.7);
	while (window.isOpen())
	{
		while (window.pollEvent(e))
		{
			if (e.type == sf::Event::Closed)
				window.close();
		}
		window.clear(sf::Color::Black);
		for (int i = 0; i < height; i++)
			for (int j = 0; j < width; j++)
			{
				if (mazeArray[i][j] == wallNoEnter)
					wallSprite.setPosition(j * 8, i * 8);
				if (mazeArray[i][j] == passEnter)
					continue;
				wallSprite.setPosition(j * 32, i * 32);
				window.draw(wallSprite);
			}
		window.display();
	}
}
////////////////////////////////
// Алгоритм построения лабиринта
void mazemake(int** mazeArray, int height, int width)
{
	int x, y, c, a;
	bool b;

	for (int i = 0; i < height; i++)
		for (int j = 0; j < width; j++)
			mazeArray[i][j] = wallNoEnter;
	// Координаты и счетчик
	x = 3;
	y = 3;
	a = 0;
	while (a < 10000)
	{
		mazeArray[y][x] = passEnter;
		a++;
		while (1)
		{
			c = rand() % 4;
			// По две клетки в одном направлении за прыжок
			switch (c)
			{ 
			case 0: if (y != 1)
				if (mazeArray[y - 2][x] == wallNoEnter)
				{
					mazeArray[y - 1][x] = passEnter;
					mazeArray[y - 2][x] = passEnter;
					y -= 2;
				}
			case 1: if (y != height - 2)
				if (mazeArray[y + 2][x] == wallNoEnter)
				{
					mazeArray[y + 1][x] = passEnter;
					mazeArray[y + 2][x] = passEnter;
					y += 2;
				}
			case 2: if (x != 1)
				if (mazeArray[y][x - 2] == wallNoEnter)
				{
					mazeArray[y][x - 1] = passEnter;
					mazeArray[y][x - 2] = passEnter;
					x -= 2;
				}
			case 3: if (x != width - 2)
				if (mazeArray[y][x + 2] == wallNoEnter)
				{
					mazeArray[y][x + 1] = passEnter;
					mazeArray[y][x + 2] = passEnter;
					x += 2;
				}
			}
			if (deadend(x, y, mazeArray, height, width))
				break;
		}
		if (deadend(x, y, mazeArray, height, width)) // Вытаскивание из тупика
			do
			{
				x = 2 * (rand() % ((width - 1) / 2)) + 1;
				y = 2 * (rand() % ((height - 1) / 2)) + 1;
			} 			while (mazeArray[y][x] != passEnter);
	}
}
int main()
{
	srand((unsigned)time(NULL));
	int height = 21, width = 21;
	int** mazeArray = new int* [height];
	for (int i = 0; i < height; i++)
		mazeArray[i] = new int[width];
	mazemake(mazeArray, height, width);
	visualSFML(mazeArray, height, width);
	for (int i = 0; i < height; i++)
		delete[] mazeArray[i];
	delete[] mazeArray;
	system("pause");
	return 0;
}