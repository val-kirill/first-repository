import pygame
pygame.init()
width = 800
height = 800
display = pygame.display.set_mode((width, height))

#sprite_image = pygame.image.load("images/sprite.png")
#sprite_rect = sprite_image.get_rect()

bg_image = pygame.image.load("images/bg.png")
bg_rect = bg_image.get_rect()
class Player:
    def __init__(self):
        self.image = pygame.image.load("images/guy1.png.")
        self.image = pygame.transform.scale(self.image, (35,70))
        self.rect = self.image.get_rect()
    def update(self):
        display.blit(self.image, self.rect)
player = Player()
run = True
while run:
    display.blit(bg_image, bg_rect)
    #display.blit(sprite_image, sprite_rect)
    player.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    pygame.quit()
class Hero:
    def __init__(self, name):
        self.name = name
        self.lives = 3
        self.level = 1
    def hello(self):
        self("привет,я" + self.name)

hero1 = Hero("Batman")
hero1.hello()
hero2 = Hero("Superman")