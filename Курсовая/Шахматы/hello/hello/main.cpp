#include <iostream>
#include <vector>
#include <string>
#include <SFML/Graphics.hpp>
#include <time.h>
#include <string>
using namespace sf;
int size = 56;
Vector2f offset(28, 28);
Sprite f[32]; // Фигуры
std::string position = "";
int board[8][8] =
{ -1,-2,-3,-4,-5,-3,-2,-1,
 -6,-6,-6,-6,-6,-6,-6,-6,
  0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0,
  0, 0, 0, 0, 0, 0, 0, 0,
  6, 6, 6, 6, 6, 6, 6, 6,
  1, 2, 3, 4, 5, 3, 2, 1 };
std::string toChessNote(Vector2f p)
{
    std::string s = "";
    s += char(p.x / size + 97);
    s += char(7 - p.y / size + 49);
    return s;
}
////////////////////////////////////////////
// Функция которая возвращает местоположение
Vector2f toCoord(char a, char b)
{
    int x = int(a) - 97;
    int y = 7 - int(b) + 49;
    return Vector2f(x * size, y * size);
}
// Есть фигуру
void move(std::string str)
{
    Vector2f oldPos = toCoord(str[0], str[1]);
    Vector2f newPos = toCoord(str[2], str[3]);
    for (int i = 0; i < 32; i++)
        if (f[i].getPosition() == newPos) f[i].setPosition(-100, -100); // Если позиция равна новой позиции фигуры то эта фигура сьедается и выносится за карту, если есть фигура на этой позиции то эта фигура сьедается
    for (int i = 0; i < 32; i++)
        if (f[i].getPosition() == oldPos) f[i].setPosition(newPos); // Если позиция равна старой позиции то фигуре присваивается новая позиция
}
/////////////////////////////////////////////////////////////
// Функция загрузки позиции по двумерному массиву board[i][j]
void loadPosition()
{
    int idFigure = 0; // Переменная в качестве id фигуры в массиве фигур
    // Перебор по двумерному массиву
    for (int i = 0; i < 8; i++)
        for (int j = 0; j < 8; j++)
        {
            int n = board[i][j]; // Присваевается n значение места фигуры в двумерном массиве board[i][j]
            if (!n) continue;
            int x = abs(n) - 1;
            int y = n > 0 ? 1 : 0;
            f[idFigure].setTextureRect(IntRect(size * x, size * y, size, size)); // Устанавливается тело обьекта для фигуры в зависимости от параметров x и y
            f[idFigure].setPosition(size * j, size * i); // Фигуры расставляются по значению перебора двумерного массива
            idFigure++;
        }
    for (int i = 0; i < position.length(); i += 5)
    {
        move(position.substr(i, 4));
        std::cout << position << std::endl;
    }
}
//////////////////////////////
// Функция управления фигурами
void controls(RenderWindow& window, Texture& board)
{
    bool isMove = false;
    Vector2f oldPos, newPos;
    float dx = 0, dy = 0;
    std::string str;
    int n = 0;
    Sprite boardSprite(board);
    while (window.isOpen())
    {
        Vector2i pos = Mouse::getPosition(window) - Vector2i(offset); // Передаются координаты мыши на экране
        Event e;
        while (window.pollEvent(e))
        {
            if (e.type == Event::Closed)
                window.close();
            // Вернуться назад
            if (e.type == Event::KeyPressed)
                if (e.key.code == Keyboard::BackSpace)
                {
                    if (position.length() > 6)  // При нажатии клавиши удаляет новые координаты и возвращается к старым координатам
                    {
                        position.erase(position.length() - 6, 5);
                    }
                    loadPosition();
                }
            // Взять и поставить
            if (e.type == Event::MouseButtonPressed)
                if (e.key.code == Mouse::Left)
                    for (int i = 0; i < 32; i++)
                        if (f[i].getGlobalBounds().contains(pos.x, pos.y))
                        {
                            isMove = true;
                            n = i;
                            dx = pos.x - f[i].getPosition().x;
                            dy = pos.y - f[i].getPosition().y;
                            oldPos = f[i].getPosition();
                        }
            if (e.type == Event::MouseButtonReleased)
                if (e.key.code == Mouse::Left)
                {
                    isMove = false;
                    Vector2f p = f[n].getPosition() + Vector2f(size / 2, size / 2);
                    newPos = Vector2f(size * int(p.x / size), size * int(p.y / size));
                    str = toChessNote(oldPos) + toChessNote(newPos);
                    move(str);
                    if (oldPos != newPos) // Если старая позиция не равняется новой позиции то новая позиция записывается в ходы и отделяется пробелом
                        position += str + " ";
                    f[n].setPosition(newPos);
                }
        }
        if (isMove)
            f[n].setPosition(pos.x - dx, pos.y - dy);
        std::cout << position << " " << str << std::endl;
        // Отрисовка
        window.clear();
        window.draw(boardSprite);
        for (int i = 0; i < 32; i++)
            f[i].move(offset);
        for (int i = 0; i < 32; i++)
            window.draw(f[i]);
        window.draw(f[n]);
        for (int i = 0; i < 32; i++)
            f[i].move(-offset);
        window.display();
    }
}
int main()
{
    RenderWindow window(VideoMode(504, 504), "Chess"); // Создается экран и задается разрешение ему, и название окна
    window.setFramerateLimit(60); // Ставится ограничение кадров
    Texture figures, board;
    figures.loadFromFile("sprites/board/figures.png");
    board.loadFromFile("sprites/board/board.png");
    for (int i = 0; i < 32; i++) f[i].setTexture(figures); // Подбирается подходящая текстура для фигуры перебором
    loadPosition();
    controls(window, board); // Функция для управления, перемещения, и отрисовки фигур
    system("pause");
    return 0;
}