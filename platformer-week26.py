import pygame
import random
from os import path

WIDTH = 800
HEIGHT = 600
FPS = 60

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 70

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BGD_COLOR = (236, 236, 236)

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

img_dir = path.join(path.dirname(__file__), 'img')
sound_dir = path.join(path.dirname(__file__), 'sound')

player_img = pygame.image.load(path.join(img_dir, 'player.png')).convert()
platform_img = pygame.image.load(path.join(img_dir, 'platform.png')).convert()

# Game loop
# Event processing
# When quit is clicked, what to do?
# When mouse is clicked, what to do?
# When keyboard is pressed, what to do?

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.set_colorkey(BGD_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH - PLAYER_WIDTH )/ 2
        self.rect.y = HEIGHT - PLAYER_HEIGHT
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, platform_sprites, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
        
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH

        if self.rect.left <= 0:
            self.rect.left = 0

        self.calc_grav()
        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, platform_sprites, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            self.change_y = 0

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 0.35
        else:
            self.change_y += 0.35

        if self.rect.y >= HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = HEIGHT - self.rect.height
            
    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, platform_sprites, False)
        self.rect.y -= 2

        if len(platform_hit_list) >0 or self.rect.bottom >= HEIGHT:
            self.change_y = -10

    def move_left(self):
        self.change_x = -6

    def move_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, ratio):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_img, (ratio * 48, 48))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def off_screen(self):
        return self.rect.top >= HEIGHT + 1

# [pos_x, pos_y, width multiplier]
levels = [
    [500, 500, 3],
    [350, 400, 2],
    [600, 300, 3]
]

all_sprites = pygame.sprite.Group()

platform_sprites = pygame.sprite.Group()
for level in levels:
    sprite = Platform(level[0], level[1], level[2])
    platform_sprites.add(sprite)
    all_sprites.add(sprite)

active_sprite = pygame.sprite.Group()
player = Player()
active_sprite.add(player)
all_sprites.add(player)

def get_top_sprite(platform_group):
    ret = None
    for sprite in platform_group:
        if ret is None or sprite.rect.top < ret.rect.top:
            ret = sprite
    return sprite

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        # Check for closing window event
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_UP:
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop()

    # Update
    top_sprite = get_top_sprite(platform_sprites)
    
    if player.rect.top < HEIGHT / 4 or player.rect.bottom <= top_sprite.rect.top:
        for sprite in all_sprites:
            sprite.rect.y += 8

    for sprite in platform_sprites:
        if sprite.off_screen():
            sprite.kill()
            new_ratio = random.randint(1, 4)
            new_x = random.randint(0, WIDTH)
            new_y = random.randint(0, top_sprite.rect.top)
            new_sprite = Platform(new_x, new_y, new_ratio)
            all_sprites.add(new_sprite)
            platform_sprites.add(new_sprite)
        
    platform_sprites.update()
    active_sprite.update()

    # Draw / Render
    screen.fill(BLACK)
    platform_sprites.draw(screen)
    active_sprite.draw(screen)

    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
