import pygame as pg
import sys

WIDTH = 360
HEIGHT = 480
WHITE = (255, 255, 255)

class Player(pg.sprite.Sprite):
    def __init__(self, imagePath):
        self.image = pg.image.load(imagePath)
        self.x, self.y = (WIDTH / 2, HEIGHT / 2)
        self.speed = 5
    def move(self, mov_tup):
        self.x += mov_tup[0]
        self.y += mov_tup[1]

def main():
    pg.init()
    pg.display.set_mode((WIDTH, HEIGHT))
    mainS = pg.display.get_surface()
    FPS = 60
    player = Player("player.png")
    clock = pg.time.Clock()
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
        mainS.fill(WHITE)
        mainS.blit(player.image, (player.x, player.y))
        pg.display.update()
        clock.tick(FPS)


main()
