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
#        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
#        self.image.fill(RED)
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
    def __init__(self, platform_def):
        pygame.sprite.Sprite.__init__(self)
#        self.image = pygame.Surface([platform_def[0], platform_def[1]])
#        self.image.fill(GREEN)
        self.image = pygame.transform.scale(platform_img, (platform_def[0], platform_def[1]))
        self.rect = self.image.get_rect()
        self.rect.x = platform_def[2]
        self.rect.y = platform_def[3]

# [width, height, pos_x, pos_y]
levels = [
    [210, 70, 500, 500],
    [100, 70, 350, 400],
    [210, 70, 600, 300]
]

platform_sprites = pygame.sprite.Group()
for platform_def in levels:
    sprite = Platform(platform_def)
    platform_sprites.add(sprite)

active_sprite = pygame.sprite.Group()
player = Player()
active_sprite.add(player)



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
            if event.key == pygame.K_LEFT and player.change_x < 0:
                player.stop()
            if event.key == pygame.K_RIGHT and player.change_x > 0:
                player.stop()

    # Update
    platform_sprites.update()
    active_sprite.update()

    # Draw / Render
    screen.fill(BLACK)
    platform_sprites.draw(screen)
    active_sprite.draw(screen)

    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
