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

font.init()
font1 = font.SysFont('Arial', 40 )
lose1 = font1.render('Player 1 lose!', True, (255, 0, 0))
lose2 = font1.render('player 2 lose!', True, (255, 0, 0))
score_text = font1.render('Счёт', True, (0, 0, 0))
score_1_text = font1.render('0', True, (80, 200, 255))
score_2_text = font1.render('0', True, (80, 200, 255))

speed_x = 4
speed_y = 2

score_1 = 0 
score_2 = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(background)
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.blit(score_text, (320, 400))

        if sprite.collide_rect(racket1, ball):
            speed_x = speed_x * -1
            score_1 += 1
            score_1_text = font1.render(str(score_1), True, (80, 200, 255))

        if sprite.collide_rect(racket2, ball):
            speed_x = speed_x * -1
            score_2 += 1
            score_2_text = font1.render(str(score_2), True, (80, 200, 255))

        if ball.rect.y < 0 or ball.rect.y > 500 -50:
            speed_y = speed_y * -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True
        
        if ball.rect.x > 700-50:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True
        
        window.blit(score_1_text,(50, 400))
        window.blit(score_2_text, (640, 400))
        racket1.update_l()
        racket2.update_r()
        racket1.reset()
        racket2.reset()    
        ball.reset()
    display.update()
    clock.tick(FPS)

