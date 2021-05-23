import pygame as pg
import sys

WIDTH = 360
HEIGHT = 480
WHITE = (255, 255, 255)

class Player(pg.sprite.Sprite):
    def __init__(self, imagePath):
        # Сначала мы устанавливаем соответствующие переменные объекта
        self.image = pg.image.load(imagePath)
        # Это координаты игрока на экране
        self.x, self.y = (WIDTH / 2, HEIGHT / 2)
        self.speed = 5
        
    def move(self, mov_tup):
        # mov_up содержит изменения, внесенные в позиции x и y, мы просто добавляем эти изменения в позицию игрока
        self.x += mov_tup[0]
        self.y += mov_tup[1]

def main():
    pg.init()
    pg.display.set_mode((WIDTH, HEIGHT)) # установка размеров окна
    mainS = pg.display.get_surface()
    FPS = 60 # Кадров в секунду
    # к главному окну теперь можно получить доступ через mainS
    player = Player("player.png")
    clock = pg.time.Clock() # обновления экрана
    mov_tup = (0, 0)
    while True:
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            elif event.type == pg.KEYDOWN:

                if event.key == pg.K_d:
                    mov_tup = (player.speed, 0)
                if event.key == pg.K_a:
                    mov_tup = (-player.speed, 0)
                if event.key == pg.K_w:
                    mov_tup = (0, -player.speed)
                if event.key == pg.K_s:
                    mov_tup = (0, player.speed)

        player.move(mov_tup)
        mainS.fill(WHITE) # Заливаем экран белым цветом
        mainS.blit(player.image, (player.x, player.y)) # Разиещяем игрока в правильную позицию
        pg.display.update()
        # перерисовываем FPS раз в секунду
        clock.tick(FPS)


main()
