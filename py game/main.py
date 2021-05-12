#подготовлено Завадским Михаилом П2-18
import pygame
from random import randrange as rnd # импортируем из модуля рандом модуль диапозона случайных чисел
from os import path

WIDTH, HEIGHT = 1200, 800
fps = 60
# настройки платформы
paddle_w = 330
paddle_h = 35
paddle_speed = 15
paddle = pygame.Rect(WIDTH // 2 - paddle_w // 2, HEIGHT - paddle_h - 10, paddle_w, paddle_h)
# настройки мячика
ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(rnd(ball_rect, WIDTH - ball_rect), HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1
# настройка блокков(которые ломает шарик)
block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)] # блоки их расположения относительно разрешения
color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for i in range(10) for j in range(4)] # разные цвета для блоков

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# фон
img = pygame.image.load('1.jpg').convert()
pygame.mixer.music.load('tgfcoder-FrozenJam-SeamlessLoop.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.0)
kn = pygame.mixer.Sound('Knock.wav')

def detect_collision(dx, dy, ball, rect): # сложная математика
    if dx > 0:
        # когда dx положительный то шарик движется в право и сталкивается с левой строной блока для отрицательного случая всё будет противоположно
        delta_x=ball.right-rect.left
    else:
        delta_x=rect.right-ball.left
        #находим аналогично x
    if dy > 0:
        delta_y=ball.bottom-rect.top
    else:
        delta_y=rect.bottom-ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy =-dx, -dy
    elif delta_x > delta_y:
        dy =-dy
    elif delta_y > delta_x:
        dx =-dx
    return dx, dy


while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            exit()
    sc.blit(img, (0, 0))
    # прорисовка мира
    [pygame.draw.rect(sc, color_list[color], block) for color, block in enumerate(block_list)] # блоки
    pygame.draw.rect(sc, pygame.Color('darkorange'), paddle) # платформа для отскоков
    pygame.draw.circle(sc, pygame.Color('white'), ball.center, ball_radius) # рисуем шарик
    # движения мячика
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy
    # коллизии лево право
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx = -dx
    # коллизия вверх
    if ball.centery < ball_radius:
        dy = -dy
    # коллизия плтформы
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # если мячик ударился мы удаляем из списка блок
    hit_index = ball.collidelist(block_list)
    if hit_index != -1:
        hit_rect = block_list.pop(hit_index)
        hit_color = color_list.pop(hit_index)
        dx, dy = detect_collision(dx, dy, ball, hit_rect)
        kn.play()
    # победа, поражение
    if ball.bottom > HEIGHT:
        print('GAME OVER!')
        exit()
    elif not len(block_list):
        print('WIN!!!')
        exit()
    # управление
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:  # конпка передвежиная + запрет выходить за поле
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < WIDTH:  # конпка передвежиная + запрет выходить за поле
        paddle.right += paddle_speed
    # обновление сцены
    pygame.display.flip()
    clock.tick(fps)
