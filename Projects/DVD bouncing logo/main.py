# DVD логотип прыгает по экрану как в старые-добрые)

import pygame as pg

pg.init()  # Инициализируем окно
pg.display.set_caption("DVD bouncer")  # Задаем заголовок окну
# Получаем информацию касательно размеров экрана
width, height = pg.display.Info().current_w, pg.display.Info().current_h
screen = pg.display.set_mode((width, height), pg.RESIZABLE)  # Открываем это окно
logo_white = pg.image.load("white_logo.png").convert()  # Загружаем картинку
logoRect = logo_white.get_rect()  # Отрисовываем для неё прямоугольник
logoSpeed = [1, 1]  # Задаём стартовую позицию
FPS = 60  # Количество прохождений цикла в секунду
FPSMode = pg.time.Clock()  # Перевод из миллисекунд в частоту обновления в секунду
# Цикл, не позволяющий игре закрыться до тех пор, пока не нажмешь нужную кнопку
cycle = True
while cycle:
    # Цикл на проверку закрытия окна. В случае закрытия окна с холстом программа закрывается
    for event in pg.event.get():
        if event.type == pg.QUIT:
            cycle = False
    screen.fill((0, 0, 0))  # Заполнение холста черным цветом
    screen.blit(logo_white, logoRect)  # Размещение объекта на холсте
    logoRect = logoRect.move(logoSpeed)  # Перемещение лого DVD по холсту
    # Если ударяется о верхнюю или нижнюю грани окна - двигается в противоположном направлении
    if logoRect.left < 0 or logoRect.right > width:
        logoSpeed[0] = -logoSpeed[0]
        logoRect = logoRect.move(logoSpeed)
        # Если ударяется о левуюю или правую грани окна - двигается в противоположном направлении
    if logoRect.top < 0 or logoRect.bottom > height:
        logoSpeed[1] = -logoSpeed[1]
        logoRect = logoRect.move(logoSpeed)
    pg.display.flip()  # Обновляем экран
    FPSMode.tick(FPS)  # Столько ждём
pg.quit()  # Выход из окна
