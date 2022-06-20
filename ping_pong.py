from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image= transform.scale(image.load(player_image), (width,height))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y

    def recet(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys=key.get_pressed()
        if keys[K_DOWN] and self.rect.y<w_height-80:
            self.rect.y+=self.speed
        if keys[K_UP] and self.rect.y>5:
            self.rect.y-=self.speed
        if keys[K_s] and self.rect.y<w_height-80:
            self.rect.y+=self.speed
        if keys[K_w] and self.rect.y>5:
            self.rect.y-=self.speed

back=(200,255,255)
w_width=600
w_height=500

win=display.set_mode((w_width,w_height))
win.fill(back)

game=True
finish=False
clock=time.Clock()
FPS=60

while True:
    display.update()
    clock.tick(FPS)

