import pygame as pg
import random

# Создание квадрата по координатам
def grect(x, y):
    return x, y, 100, 100

# Создание окна с разрешением
pg.init()
sc = pg.display.set_mode((700, 500))
cl = pg.time.Clock()

# Создание переменных и списка
x, y = 100, 200
t = True
color = ''
colorAll = ['white', 'orange', 'blue', 'green', 'red', 'yellow']

# Запуск цикла
while 1:
  
  # Задаем цвет фона
  sc.fill(pg.Color("black"))
  
  # Проверка на закрытие окна
  [exit() for event in pg.event.get() if event.type == pg.QUIT]
  
  # Переключение режимов
  if x == 100:
    t = False
    color = random.choice(colorAll)
  elif x == 200:
    t = True
    color = random.choice(colorAll)
  
  # События режимов
  if t == True:
    x -= 1
  else:
    x += 1
    pg.draw.rect(sc, pg.Color("white"), (100, 50, 100, 100))
  
  # Создание статичных квадратов
  pg.draw.rect(sc, pg.Color("white"), grect(x, y))
  pg.draw.rect(sc, pg.Color(color), (100, 350, 100, 100))
  
  # Обновление ока с заданным тиком
  pg.display.flip()
  cl.tick(60)
