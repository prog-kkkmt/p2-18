import pygame
import sys
import random
import queue

from pygame.color import THECOLORS


def up_step(y, wight):
    if y > wight * 0.08:
        return y - wight * 0.015
    else:
        return y


def down_step(y, wight):
    if y < wight - (wight * 0.08):
        return y + wight * 0.015
    else:
        return y


def left_step(x, wight):
    if x > wight * 0.08:
        return x - wight * 0.015
    return x


def right_step(x, wight):
    if x < wight - (wight * 0.08):
        return x + wight * 0.015
    return x


def move(x, y):
    if keys[pygame.K_UP]:
        y = float(up_step(y, wight))
    if keys[pygame.K_DOWN]:
        y = float(down_step(y, wight))
    if keys[pygame.K_LEFT]:
        x = float(left_step(x, wight))
    if keys[pygame.K_RIGHT]:
        x = float(right_step(x, wight))
    return x, y


def game_over(gg):
    font = pygame.font.SysFont('couriernew', int(wight * 0.06))
    text = font.render(str('GAME OVER'), True, THECOLORS['red'])
    screen.blit(text, (wight * 0.14, wight * 0.45))
    pygame.display.flip()


def draw_circle(wight):
    pygame.draw.circle(screen, THECOLORS['gray'], (x, y), wight * 0.07)
    pygame.draw.circle(screen, (100, 0, 245), (x, y), (wight * 0.07 * 0.5))


def menu(position, wight):
    font = pygame.font.SysFont('couriernew', int(wight * 0.06))
    start = font.render(str('START'), True, THECOLORS['green'] if (position == 1) else THECOLORS['pink'])
    settings = font.render(str('SETTINGS'), True, THECOLORS['green'] if (position == 2) else THECOLORS['pink'])
    exitt = font.render(str('EXIT'), True, THECOLORS['green'] if (position == 3) else THECOLORS['pink'])
    screen.blit(start, (wight * 0.4, wight * 0.2))
    screen.blit(settings, (wight * 0.35, wight * 0.3))
    screen.blit(exitt, (wight * 0.425, wight * 0.4))
    # event.type = pygame.MOUSEBUTTONDOWN, event.button = 3, event.pos = (100, 100).

    if event.type == pygame.MOUSEMOTION and event.pos[0] > wight * 0.4 and event.pos[0] < wight * 0.57 and event.pos[
        1] > wight * 0.4 and event.pos[1] < wight * 0.45:
        position = 3
    elif event.type == pygame.MOUSEBUTTONUP and event.pos[0] > wight * 0.4 and event.pos[0] < wight * 0.57 and \
            event.pos[1] > wight * 0.4 and event.pos[1] < wight * 0.45:
        position = 33
    elif event.type == pygame.MOUSEMOTION and event.pos[0] > wight * 0.4 and event.pos[0] < wight * 0.57 and event.pos[
        1] > wight * 0.2 and event.pos[1] < wight * 0.25:
        position = 1
    elif event.type == pygame.MOUSEBUTTONUP and event.pos[0] > wight * 0.4 and event.pos[0] < wight * 0.57 and \
            event.pos[1] > wight * 0.2 and event.pos[1] < wight * 0.25:
        position = 11
    elif event.type == pygame.MOUSEMOTION and event.pos[0] > wight * 0.33 and event.pos[0] < wight * 0.65 and event.pos[
        1] > wight * 0.3 and event.pos[1] < wight * 0.35:
         position = 2
    elif event.type == pygame.MOUSEBUTTONUP and event.pos[0] > wight * 0.33 and event.pos[0] < wight * 0.65 and event.pos[
        1] > wight * 0.3 and event.pos[1] < wight * 0.35:
        position = 22
    return position


def setting(wight, position,sizr_check,no_wight):
    font = pygame.font.SysFont('couriernew', int(wight * 0.06))
    size = font.render(str('Size:'), True, THECOLORS['green'] if (sizr_check == 1) else THECOLORS['pink'])
    screen.blit(size, (wight * 0.4, wight * 0.2))
    if event.type == pygame.MOUSEMOTION and event.pos[0] > wight * 0.4 and event.pos[0] < wight * 0.57 and event.pos[1] > wight * 0.2 and event.pos[1] < wight * 0.25:
        sizr_check = 1
    if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
        position = 0
        wight = INTEGER(no_wight,wight)
        no_wight = ''
    elif event.type == pygame.KEYUP and event.key == pygame.K_BACKSPACE:
        no_wight = no_wight[:-1]
    elif event.type == pygame.KEYUP:
        no_wight += event.unicode
    size = font.render(str(no_wight), True, THECOLORS['pink'])
    screen.blit(size, (wight * 0.6, wight * 0.2))
    return wight, position,sizr_check,no_wight

def INTEGER(no_wight,wight):
    try:
        return int(no_wight)
    except:
        return int(wight)


pygame.init()

# Переменные и счетчики

# wight=int(input("wight"))
wight = 750
x = wight / 2
y = x
temp = 0
home_hub = queue.Queue()
limit = 0
first = 0
second = 0
i = 0
gg = 0
position = 0
sizr_check=0
no_wight=''

while True:
    # Создание экрана
    hight = wight
    if position == 0:
        x = wight / 2
        y = x
    screen = pygame.display.set_mode((wight, hight))
    # Ограничение FPS
    pygame.time.delay(10)
    # Условия выключения приложения
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    # Проигрыш
    if gg == 1:
        game_over(gg)
        '''
        pygame.key.get_pressed()
        sd = ''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(sd)
                sd = ''
            elif event.key == pygame.K_BACKSPACE:
                sd = sd[:-1]
            else:
                sd += event.unicode
        print(sd)'''
        if event.type == pygame.MOUSEBUTTONUP:
            hight = wight
            x = wight / 2
            y = x
            temp = 0
            home_hub = queue.Queue()
            limit = 0
            first = 0
            second = 0
            i = 0
            gg = 0
            position = 0
            sizr_check=0
        continue

    keys = pygame.key.get_pressed()

    # Создание меню
    if position == 22:
        wight, position,sizr_check,no_wight = setting(wight, position,sizr_check,no_wight)
    elif position == 33:
        pygame.quit()
        sys.exit()
    elif position == 11:

        # Отрисовка круга
        draw_circle(wight)

        # Создание преград
        temp += 1
        if temp == 20:
            rx = 0
            ry = random.randrange(round(wight * 0.07), round(wight - (wight * 0.08)))
            temp = random.randrange(-40, -20)
            if limit != 5:
                limit += 1
                home_hub.put(ry)
                home_hub.put(rx)
        # Отрисовка и обработка преград
        if not home_hub.empty():
            for i in range(limit):
                first = home_hub.get()
                second = home_hub.get()
                if first != 0 and second != first:
                    pygame.draw.rect(screen, THECOLORS['gray'], (first, second, wight * 0.1, wight * 0.1))

                    # Сканирование столкновений преград с кругом
                    # (X - Xo)^2 +(Y - Yo)^2 <= R^2

                    if (first - x) ** 2 + (second - y) ** 2 <= (wight * 0.07) ** 2 or (first + wight * 0.1 - x) ** 2 + (
                            second - y) ** 2 <= (wight * 0.07) ** 2 or (first - x) ** 2 + (
                            second + wight * 0.1 - y) ** 2 <= (
                            wight * 0.07) ** 2 or (first + wight * 0.1 - x) ** 2 + (second + wight * 0.1 - y) ** 2 <= (
                            wight * 0.07) ** 2:
                        gg = 1
                # Уничтожение преград, что вышли за экран
                if second < wight:
                    home_hub.put(first)
                    home_hub.put(second + wight * 0.004)
                else:
                    limit -= 1

        # Движение круга
        x, y = move(x, y)
    elif position != 11:
        position = menu(position, wight)

    pygame.display.flip()

