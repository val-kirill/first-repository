
import pygame
import json

pygame.init()
width = 800
height = 800
tile_size = 40
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Platformer Game")

# Загрузка данных уровня и фоновое изображение
with open("levels/level1.json", "r") as file:
    world_data = json.load(file)

bg_image = pygame.image.load("images/bg.png")
bg_rect = bg_image.get_rect()


# Класс игрока
class Player:
    def init(self, data):
        dirt_img = pygame.image.load("images/walk1.png")
        grass_img = pygame.image.load("images/walk2.png")
        self.tile_list = []
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1 or tile == 2:
                    images = {1: dirt_img, 2: grass_img}
                    img = pygame.transform.scale(images[tile], (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tile_list.append((img, img_rect))
                col_count += 1
            row_count += 1

        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        self.direction = 0
        for num in range(1, 4):
            img_right = pygame.image.load(f"images/walk{num}.png")
            img_right = pygame.transform.scale(img_right, (35, 70))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 600
        self.gravity = 0
        self.jumped = False

    def update(self):
        x = 0
        y = 0
        walk_speed = 10
        key = pygame.key.get_pressed()

        # Прыжок
        if key[pygame.K_SPACE] and not self.jumped:
            self.gravity = -15
            self.jumped = True

        # Движение влево
        if key[pygame.K_LEFT]:
            x -= 5
            self.direction = -1
            self.counter += 1

        # Движение вправо
        if key[pygame.K_RIGHT]:
            x += 5
            self.direction = 1
            self.counter += 1

        # Анимация ходьбы
        if self.counter > walk_speed:
            self.counter = 0
            self.index += 1
        if self.index >= len(self.images_right):
            self.index = 0
        if self.direction == 1:
            self.image = self.images_right[self.index]
        elif self.direction == -1:
            self.image = self.images_left[self.index]

        # Гравитация
        self.gravity += 1
        if self.gravity > 10:
            self.gravity = 10
        y += self.gravity

        # Обновление позиции
        self.rect.x += x
        self.rect.y += y

        # Ограничение по земле
        if self.rect.bottom > height:
            self.rect.bottom = height
            self.jumped = False

        # Отрисовка игрока
        display.blit(self.image, self.rect)


# Класс мира
class World:
    def init(self, data):
        tile1_img = pygame.image.load("images/tile1.png")
        grass_img = pygame.image.load("images/tile4.png")
        self.tile_list = []
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1 or tile == 2:
                    images = {1: tile1_img, 2: grass_img}
                    img = pygame.transform.scale(images[tile], (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    self.tile_list.append((img, img_rect))
                elif tile == 3:
                    lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
                    lava_group.add(lava)
                col_count += 1
            row_count += 1

    def draw(self):
        pass


def draw(self):
        for tile in self.tile_list:
            display.blit(tile[0], tile[1])


# Класс лавы
class Lava(pygame.sprite.Sprite):
    def init(self, x, y):
        super().init()
        img = pygame.image.load("images/tile6.png")
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


lava_group = pygame.sprite.Group()

# Создание мира и игрока
world = World()
player = Player()

# Игровой цикл
run = True
while run:
    display.blit(bg_image, bg_rect)

    # Обновление и отрисовка объектов
    world.draw()
    lava_group.draw(display)
    lava_group.update()
    player.update()

    # События
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()