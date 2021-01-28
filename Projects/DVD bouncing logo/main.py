# DVD логотип прыгает по экрану как в старые-добрые)

import pygame as pg
import random as rnd

pg.init()  # Инициализируем окно
pg.display.set_caption("DVD bouncer")  # Задаем заголовок окну
# Получаем информацию касательно размеров экрана
width, height = pg.display.Info().current_w, pg.display.Info().current_h
screen = pg.display.set_mode((width, height), pg.FULLSCREEN)  # Открываем это окно
logo1 = pg.image.load("white_logo.png").convert()  # Загружаем картинки
logo2 = pg.image.load("orange_logo.png").convert()
logo3 = pg.image.load("red_logo.png").convert()
logo4 = pg.image.load("blue_logo.png").convert()
logo5 = pg.image.load("light_blue_logo.png").convert()
logo6 = pg.image.load("green_logo.png").convert()
logo7 = pg.image.load("light_green_logo.png").convert()
secret_logo = pg.image.load("black_logo.png").convert()
logos = [logo1, logo2, logo3, logo4, logo5, logo6, logo7]  # Список логотипов
random_logo = rnd.choice(logos)  # Случайный выбор лого из списка
logoRect = random_logo.get_rect()  # Отрисовываем для неё прямоугольник
logoSpeed = [3, 3]  # Задаём скорость передвижения
FPS = 60  # Количество прохождений цикла в секунду
FPSMode = pg.time.Clock()  # Перевод из миллисекунд в частоту обновления в секунду

# Цикл, не позволяющий игре закрыться до тех пор, пока не нажмешь нужную кнопку
cycle = True
while cycle:
    # Цикл на проверку закрытия окна. В случае закрытия окна с холстом или нажатия "пробел" программа закрывается
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cycle = False
    # Если ударяется о верхнюю или нижнюю грани окна - двигается в противоположном направлении
    if logoRect.left < 0 or logoRect.right > width:
        logoSpeed[0] = -logoSpeed[0]
        logoRect = logoRect.move(logoSpeed)
        random_logo = rnd.choice(logos)  # Замена логотипа
    # Если ударяется о левуюю или правую грани окна - двигается в противоположном направлении
    if logoRect.top < 0 or logoRect.bottom > height:
        logoSpeed[1] = -logoSpeed[1]
        logoRect = logoRect.move(logoSpeed)
        random_logo = rnd.choice(logos)  # Замена логотипа
    # В случае, если попадет в какой-либо УГОЛ - закроется
    if logoRect.left < 0 and logoRect.right > width or logoRect.top < 0 and logoRect.bottom > height:
        random_logo = secret_logo
        cycle = False
        print("Конец...")
    screen.fill((0, 0, 0))  # Заполнение холста черным цветом
    screen.blit(random_logo, logoRect)  # Размещение объекта на холсте
    logoRect = logoRect.move(logoSpeed)  # Перемещение лого DVD по холсту
    pg.display.flip()  # Обновляем экран
    FPSMode.tick(FPS)  # Столько ждём
pg.display.quit()  # Выход из окна
pg.quit()
