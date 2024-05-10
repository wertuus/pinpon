#Создай собственный Шутер!
from random import *
from pygame import *
from time import time as timer
window = display.set_mode((700, 500))
display.set_caption('lol')
background = (200, 255, 255)
window.fill(background)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed

racket1 = Player('racket.png', 30, 200, 50, 150, 4)
racket2 = Player('racket.png', 620, 200, 50, 150, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)

clock = time.Clock()
FPS = 160

game =  True
finish = False
num_fire = 0

font.init()
font1 = font.SysFont('Arial', 80 )
win = font1.render('YOU WIN!', True, (255, 255, 255))
lose = font1.render('YOU LOSE!', True, (180, 0, 0))
font2 = font.SysFont('Arial', 36)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(background)
        racket1.update_l()
        racket2.update_r()
        racket1.reset()
        racket2.reset()
        display.update()

    clock.tick(FPS)

