#include <stdlib.h>
#include <time.h>
using namespace std;

int** maze;
const int wall = 0, pass = 1;
// ��������������� �������, ���������� ������
bool deadend(int x, int y, int** maze, int height, int width)
{
    int a = 0;

    if (x > 1) {
        if (maze[y][x - 2] == pass)
            a += 1;
    }
    else a += 1;

    if (y > 1) {
        if (maze[y - 2][x] == pass)
            a += 1;
    }
    else a += 1;

    if (x < width - 2) {
        if (maze[y][x + 2] == pass)
            a += 1;
    }
    else a += 1;

    if (y < height - 2) {
        if (maze[y + 2][x] == pass)
            a += 1;
    }
    else a += 1;

    if (a == 4)
        return 1;
    else
        return 0;
}
// ���������� ��������
void mazemake(int** maze, int height, int width)
{
    int x, y, c, a;
    bool b;

    for (int i = 0; i < height; i++) // ������ ����������� ������-��������
        for (int j = 0; j < width; j++)
            maze[i][j] = wall;

    x = 3; y = 3; a = 0; // ����� ����������� ����� � �������
    while (a < width * height) { // ��, ��������, �������, ����� ���� ���, �� ����
        maze[y][x] = pass; a++;
        while (1) { // ����������� ����, ������� ����������� ������ �������
            c = rand() % 4; // ���������, ��� ���� ���������
            switch (c) {  // �� ��� ������ � ����� ����������� �� ������
            case 0: if (y > 1)
                if (maze[y - 2][x] == wall) { // �����
                    maze[y - 1][x] = pass;
                    maze[y - 2][x] = pass;
                    y -= 2;
                }
            case 1: if (y < height - 2)
                if (maze[y + 2][x] == wall) { // ����
                    maze[y + 1][x] = pass;
                    maze[y + 2][x] = pass;
                    y += 2;
                }
            case 2: if (x > 1)
                if (maze[y][x - 2] == wall) { // ������
                    maze[y][x - 1] = pass;
                    maze[y][x - 2] = pass;
                    x -= 2;
                }
            case 3: if (x < width - 2)
                if (maze[y][x + 2] == wall) { // �������
                    maze[y][x + 1] = pass;
                    maze[y][x + 2] = pass;
                    x += 2;
                }
            }
            if (deadend(x, y, maze, height, width))
                break;
        }

        if (deadend(x, y, maze, height, width)) // ����������� ����� �� ������
            do {
                x = 2 * (rand() % ((width - 1) / 2)) + 1;
                y = 2 * (rand() % ((height - 1) / 2)) + 1;
            } while (maze[y][x] != pass);
    } // �� ���� � ���.
}

void CreateMaze(int width, int height)
{
    srand(time(NULL));

    maze = new int* [width];
    for (int i = 0; i < width; i++)
        maze[i] = new int[height];

    if(width%2 == 0)
        mazemake(maze, width - 1, height);
    else
    if(height%2 == 0)
        mazemake(maze, width, height - 1);
    else
    if(width % 2 == 0 && height % 2 == 0)
        mazemake(maze, width - 1, height - 1);
    else
        mazemake(maze, width, height);
}