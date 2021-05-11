import pygame
import sys

from pygame.color import THECOLORS

flip=0
x = 0
pygame.init()

while True:
#Создание экрана
    screen = pygame.display.set_mode((500, 500))
#Условия окончания программы
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
#Огранечение FPS
    pygame.time.delay(200)


#Сканирование нажатия клавиши и дальнейшие действия в зависимости от нажатой клавиши
    keys = pygame.key.get_pressed()

    if event.type == pygame.KEYUP and event.key == pygame.K_KP_ENTER:
        if x==0:
            x=1
        else:
            x=0


    if event.type == pygame.KEYUP and event.key == pygame.K_5:
        if flip == 1:
            flip = 0
        else:
            flip = 1


    if flip == 1:
        pygame.draw.rect(screen, THECOLORS['white'], (0, 0, 250, 250), 2)


#Настройка шрифтов текста
    font = pygame.font.SysFont('couriernew', 40)
    hello_help = pygame.font.SysFont('none', 20)


#Вывод текста
    text = hello_help.render(str('Press 5 to show center.'), True, THECOLORS['blue'])
    screen.blit(text, (160, 70))
    text = hello_help.render(str('Press NUMPAD ENTER to swap text.'), True, THECOLORS['blue'])
    screen.blit(text, (120, 100))
    if x==0:
        pygame.draw.rect(screen, THECOLORS['green'], (60, 225, 370, 40), 2)
        text = font.render(str('HELLO, WORLD!!!'), True, THECOLORS['red'])
        screen.blit(text, (70, 225))
    else:
        pygame.draw.rect(screen, THECOLORS['red'], (180, 225, 140, 40), 2)
        text = font.render(str('HELLO'), True, THECOLORS['green'])
        screen.blit(text, (190, 225))


#Обновление экрана
    pygame.display.flip()