import pygame
pygame.init()

width = 800
height = 800
clock = pygame.time.Clock()
fps = 60
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Platformer")

sprite_image = pygame.image.load("images/guy1.png")
sprite_rect = sprite_image.get_rect()
bg_image = pygame.image.load("images/bg.png")
bg_rect = bg_image.get_rect()
run = True
while run:
    clock.tick(fps)
    display.blit(bg_image, bg_rect)
    display.blit(sprite_image, sprite_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        pygame.display.update()
pygame.init()
width = 800
height = 800
display = pygame.display.set_mode((width, height))

#sprite_image = pygame.image.load("images/sprite.png")
#sprite_rect = sprite_image.get_rect()

bg_image = pygame.image.load("images/bg.png")
bg_rect = bg_image.get_rect()
class World:
    def __init__(self, data):

        self.tile_list = []
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1 or tile == 2:
                    images = { 1: dirt_img, 2:grass_img }
                    img = pygame.transform.scale(images[tile],
                                            (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)

                    def draw(self):
                        for tile in self.tile_list:
                            display.blit(tile[0], tile[1])
world = World(world_data)
player = Player()
run = True
while run:
    display.blit(bg_image, bg_rect)
    # display.blit(sprite_image, sprite_rect)
    player.update()
    world.draw()
    player.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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
    world.draw()
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
pygame.quit()
with open("levels/levell.json", "r") as file:
    world_data = json.load(file)
    def __init__(self):
        self.image = pygame.image.load("img/guy1.png")
        self.image = pygame.transform.scale("self.image, (35,70)")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = height - 130
def update(self):
    x = 0
    y = 0
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x -= 5
    if key[pygame.K_RIGHT]:
        x +=5
    self.gravity += 1
    if self.gravity > 10:
        self.gravity = 10
    y +=  self.gravity
    self.rect.x += x
    self.rect.y += y
    display.blit(self.image, self.rect)
player = Player()
run = True
while run:
    clock.tick(fps)
    display.blit(bg_image, bg_rect)
    player.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        pygame.display.update()
    pygame.quit()
class Player:
    def __init__(self):
        self.image_right = []
        self.image_left = []
        self.index = 0
        self.counter = 0
        self.direction = 0
        self.direction = 0
        for num in range(1, 4):
            img_right = pygame.image.load(f"img/player{num}/png")
            img_right = pygame.transform.scale(img_right, (35, 70))
            img_left = pygame.transform.flip(img_right, True, False)
            self.image_right.append(img_right)
            self.image_left.append(img_left)
        self.image = self.image_right[self.index]
        self.counter += 1
        if self.counter > walk_speed:
            self.index += 1
        if self.index >= len(self.image_right):
            self.index = 0
        if self.direction == 1:
            self.image = self.images_right[self.index]
        else:
            self.image = self.images_left[self.index]





