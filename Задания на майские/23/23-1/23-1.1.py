# Выполнил Кузнецов М. С. П2-18.

# Задание 1-1.
# В модуле pygame.display есть функция set_caption().
# Ей передается строка, которую она устанавливает в качестве заголовка окна.
# Сделайте так, чтобы каждую секунду заголовок окна изменялся.

import pygame
import random

size = width, height = 800, 600
black = 0, 0, 0
numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        while not end:
            screen.fill(black)
            pygame.time.wait(1000)
            pygame.display.set_caption(random.choice(numbers))


if __name__ == '__main__':
    main()
    pygame.quit()
