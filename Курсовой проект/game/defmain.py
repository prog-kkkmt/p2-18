import pygame
from pygame.locals import *

# Функция для возвращения мяча на центр поля
def resetPuck():
    discVelocity[0] = 5 * serveDirection
    discVelocity[1] = 5 * serveDirection
    print(score1, score2)
    disc.x = screen.get_width() / 2
    disc.y = screen.get_height() / 2

# Функция для отображения текста на экране
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

# Функция для меню (паузы)
def pause():
    paused = True
    message_to_screen("Paused", black, -100, size="large")
    message_to_screen("Press c to continue , q to quit", black, 25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        clock.tick(5)

# Функция для отображения текста на экране
def message_to_screen(msg, color, y_displace=0, x_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (screen.get_width() / 2 + x_displace), ((screen.get_height() / 2) + y_displace)
    screen.blit(textSurf, textRect)

# Основной цикл игры
def gameLoop():
    gameExit = False
    score1, score2 = 0, 0
    while not gameExit:
        for event in pygame.event.get():
            down2, up2, up, down, left2, right2, right, left = 0, 0, 0, 0, 0, 0, 0, 0
            print(event)
            if event.type == pygame.QUIT:
                gameExit = True
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                left = 1
            elif keys[K_RIGHT]:
                right = 1
            elif keys[K_UP]:
                up = 1
            elif keys[K_DOWN]:
                down = 1
            keys = pygame.key.get_pressed()
            if keys[K_a]:
                left2 = 1
            elif keys[K_d]:
                right2 = 1
            elif keys[K_w]:
                up2 = 1
            elif keys[K_s]:
                down2 = 1
            elif keys[K_p]:
                pause()

        # Цикл для первого игрока
        paddle1.y += (down2 - up2) * paddleVelocity
        paddle1.x += (right2 - left2) * paddleVelocity
        if paddle1.y < 0:
            paddle1.y = 0
        elif paddle1.y > screen.get_height() - paddle1.height:
            paddle1.y = screen.get_height() - paddle1.height
        if paddle1.x < 0:
            paddle1.x = 0
        elif paddle1.x > screen.get_width() / 2 - paddle1.width:
            paddle1.x = screen.get_width() / 2 - paddle1.width

        # Цикл для второго игрока
        paddle2.y += (down - up) * paddleVelocity
        paddle2.x += (right - left) * paddleVelocity
        if paddle2.y < 0:
            paddle2.y = 0
        elif paddle2.y > screen.get_height() - paddle2.height:
            paddle2.y = screen.get_height() - paddle2.height
        if paddle2.x > screen.get_width() - paddle1.width:
            paddle2.x = screen.get_width() - paddle1.width
        elif paddle2.x < screen.get_width() / 2:
            paddle2.x = screen.get_width() / 2

        # Цикл для мяча
        disc.x += discVelocity[0]
        disc.y += discVelocity[1]
        if disc.colliderect(goal1):
            score2 += 1
            resetPuck()
        if disc.colliderect(goal2):
            score1 += 1
            resetPuck()
        if disc.y - 10 < 0 or disc.y + 10 > screen.get_height() - disc.height:
            discVelocity[1] *= -1
        if disc.colliderect(paddle1) or disc.colliderect(paddle2):
            discVelocity[0] *= -1
        if disc.x - 10 < 0 or disc.x + 25 > screen.get_width():
            discVelocity[0] *= -1

        # Рендер, наполнение игрового поля, отрисовка мяча и игроков
        screen.fill(green)
        message_to_screen("Player 1", black, -250, -150, "small")
        message_to_screen(str(score1), black, -200, -150, "small")
        message_to_screen("Player 2", black, -250, 150, "small")
        message_to_screen(str(score2), black, -200, 150, "small")
        message_to_screen("P = pause", black, -275, -325, "small")
        pygame.draw.rect(screen, (255, 100, 100), paddle1)
        pygame.draw.rect(screen, (20, 20, 100), paddle2)
        pygame.draw.rect(screen, light_blue, goal1)
        pygame.draw.rect(screen, light_blue, goal2)
        screen.blit(img, (disc.x, disc.y))
        screen.blit(bluepadimg, (paddle1.x - 5, paddle1.y - 5))
        screen.blit(redpadimg, (paddle2.x - 5, paddle2.y - 5))
        pygame.draw.circle(screen, white, (screen.get_width() / 2, screen.get_height() / 2), screen.get_width() / 10, 5)

        # Отрисовка границ и центра игровой зоны
        pygame.draw.line(screen, white, divline1, divline2, 5)
        pygame.draw.line(screen, white, (0, 0), (screen.get_width() / 2 - 5, 0), 5)
        pygame.draw.line(screen, white, (0, screen.get_height()), (screen.get_width() / 2 - 5, screen.get_height()), 5)
        pygame.draw.line(screen, white, (screen.get_width() / 2 + 5, 0), (screen.get_width(), 0), 5)
        pygame.draw.line(screen, white, (screen.get_width() / 2 + 5, screen.get_height()),
                         (screen.get_width(), screen.get_height()), 5)
        pygame.draw.line(screen, white, (0, 0), (0, screen.get_height() / 2 - goalheight), 5)
        pygame.draw.line(screen, white, (0, screen.get_height() / 2 + goalheight), (0, screen.get_height()), 5)
        pygame.draw.line(screen, white, (screen.get_width(), 0),
                         (screen.get_width(), screen.get_height() / 2 - goalheight), 5)
        pygame.draw.line(screen, white, (screen.get_width(), screen.get_height() / 2 + goalheight),
                         (screen.get_width(), screen.get_height()), 5)
        pygame.display.update()
        clock.tick(60)


gameLoop()
