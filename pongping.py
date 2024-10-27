
from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Bot(GameSprite):
    def auto_play(self, ball_y):
        difference = ball_y - self.rect.y 
        if difference < 0:
            self.rect.y -= randint(2, 4)
        else:
            self.rect.y += randint(2, 4)

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False

playerLeft = Player("wall.png", 10, 250, 5, 25, 100)
playerRight = Player("wall.png", 565, 250, 5, 25, 100)
ball = Player("ball.png", 300, 250, 5, 50, 50)

font.init()
font1 = font.Font(None, 70)
text_1 = font1.render("LEFT VICTORY!", True, (255,0,0))
text_2 = font1.render("RIGHT VICTORY!", True, (255,0,0))

FPS = 50
clock = time.Clock()

ball_speed_x = ball.speed
ball_speed_y = ball.speed

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill((200, 255, 255))

        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y
        
        if sprite.collide_rect(ball, playerLeft):
            ball_speed_x = ball.speed

        if sprite.collide_rect(ball, playerRight):
            ball_speed_x = -ball.speed

        if ball.rect.y > win_height - 50:
            ball_speed_y = -ball.speed
        
        if ball.rect.y < 0:
            ball_speed_y = ball.speed

        if ball.rect.x < 0:
            window.blit(text_1, (win_width/5, win_height/2))
            finish = True

        if ball.rect.x > win_width - 50:
            window.blit(text_2, (win_width/5, win_height/2))
            finish = True

        playerLeft.update_l()
        playerRight.update_r()

        playerLeft.reset()
        playerRight.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
