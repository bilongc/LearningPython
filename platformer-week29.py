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
IMG_BGD_COLOR = (0,155,155)

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

img_dir = path.join(path.dirname(__file__), 'img')
sound_dir = path.join(path.dirname(__file__), 'sound')

player_img = pygame.image.load(path.join(img_dir, 'player.png')).convert()

# Game loop
# Event processing
# When quit is clicked, what to do?
# When mouse is clicked, what to do?
# When keyboard is pressed, what to do?
class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.set_colorkey(BGD_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = (WIDTH - PLAYER_WIDTH )/ 2
        self.rect.y = HEIGHT - PLAYER_HEIGHT
        self.change_x = 0
        self.change_y = 0
        self.sprite_sheet = sprite_sheet
        self.load_images()
        self.dir = 'r'
        self.current_frame = 0
        self.last_updated = 0
        self.walking = False
        self.life = 3

    def load_images(self):
        self.image_running_l = []
        self.image_running_r = []
        self.image_standing_l = []
        self.image_standing_r = []

        for x in range(0, 476, 68):
            image = pygame.transform.scale(self.sprite_sheet.get_image(x, 0, 68, 100), (PLAYER_WIDTH, PLAYER_HEIGHT))
            image.set_colorkey(IMG_BGD_COLOR)
            self.image_running_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.image_running_l.append(image)

        for x in range(0, 204, 68):
            image = pygame.transform.scale(self.sprite_sheet.get_image(x, 100, 68, 100), (PLAYER_WIDTH, PLAYER_HEIGHT))
            image.set_colorkey(IMG_BGD_COLOR)
            self.image_standing_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.image_standing_l.append(image)

    def animate(self):
        now = pygame.time.get_ticks()

        if self.walking:
            if now - self.last_updated > 75:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % 6
                if self.dir == 'r':
                    self.image = self.image_running_r[self.current_frame]
                else:
                    self.image = self.image_running_l[self.current_frame]
        else:
            if now - self.last_updated > 75:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % 2
                if self.dir == 'r':
                    self.image = self.image_standing_r[self.current_frame]
                else:
                    self.image = self.image_standing_l[self.current_frame]

    def update(self):
        self.animate()
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
        self.dir = 'l'
        self.walking = True

    def move_right(self):
        self.change_x = 6
        self.dir = 'r'
        self.walking = True

    def stop(self):
        self.change_x = 0
        self.walking = False


class Enemy(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, mid_x, bottom):
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = sprite_sheet
        self.current_frame = 0
        self.frames_l = []
        self.frames_r = []
        self.last_updated = 0
        for y in range(240, 336, 48):
            for x in range(0, 395, 79):
                image = sprite_sheet.get_image(x, y, 79, 48)
                self.frames_r.append(image)
                image = pygame.transform.flip(image, True, False)
                self.frames_l.append(image)
        if random.randrange(2) == 0:
            self.dir = 'l'
            self.current_frame = random.randrange(len(self.frames_l))
            self.image = self.frames_l[self.current_frame]
        else:
            self.dir = 'r'
            self.current_frame = random.randrange(len(self.frames_r))
            self.image = self.frames_r[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.centerx = mid_x
        self.rect.bottom = bottom

    def update(self):
        self.animate()

    def animate(self):
        now = pygame.time.get_ticks()
        if now - self.last_updated > 175:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % 10
            if self.dir == 'l':
                self.image = self.frames_l[self.current_frame]
            else:
                self.image = self.frames_r[self.current_frame]

class Platform(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, x, y, ratio):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.get_image(0, 384, ratio*48, 48)
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

class SpriteSheet:
    def __init__(self, filename):
        self.sprite_sheet = pygame.image.load(path.join(img_dir, filename)).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height])
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image

all_sprites = pygame.sprite.Group()

sprite_sheet = SpriteSheet('jump_sprites_sm.png')
platform_sprites = pygame.sprite.Group()
for level in levels:
    sprite = Platform(sprite_sheet, level[0], level[1], level[2])
    platform_sprites.add(sprite)
    all_sprites.add(sprite)

active_sprite = pygame.sprite.Group()
player = Player(sprite_sheet)
active_sprite.add(player)
all_sprites.add(player)

enemy = Enemy(sprite_sheet, 700, 300)
active_sprite.add(enemy)
all_sprites.add(enemy)

def get_top_sprite(platform_group):
    ret = None
    for sprite in platform_group:
        if ret is None or sprite.rect.top < ret.rect.top:
            ret = sprite
    return ret


# process_events will process the event queue, and return whether QUIT button is clicked
# or not
def process_events():
    for event in pygame.event.get():
        # Check for closing window event
        if event.type == pygame.QUIT:
            return True
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

    return False


def get_new_platform(near):
        new_ratio = random.randint(1, 4)
        mid = (near.rect.left + near.rect.right) / 2
        if mid > WIDTH / 2:
            new_x = random.randint(near.rect.left - 80 - new_ratio*48, near.rect.left - new_ratio * 48 - 50)
        else:
            new_x = random.randint(near.rect.right + 30, near.rect.right + 100)
        new_y = random.randint(near.rect.top - 120, near.rect.top - 100)
        return Platform(sprite_sheet, new_x, new_y, new_ratio)


def draw_heart(screen, sprite_sheet, life):
    img = sprite_sheet.get_image(450, 45, 50, 45)
    img.set_colorkey(IMG_BGD_COLOR)
    rect = img.get_rect()
    for i in range(life):
        rect.x = i * 50
        rect.y = 10
        screen.blit(img, rect)

running = True
while running:
    clock.tick(FPS)

    # Process input events
    if process_events():
        running = False

    # Update
    top_sprite = get_top_sprite(platform_sprites)
    
    if player.change_y == 0 and (player.rect.top < HEIGHT / 4 or player.rect.bottom <= top_sprite.rect.top):
        for sprite in all_sprites:
            sprite.rect.y += 8

    for sprite in platform_sprites:
        if sprite.off_screen():
            sprite.kill()
            new_sprite = get_new_platform(top_sprite)
            all_sprites.add(new_sprite)
            platform_sprites.add(new_sprite)
        
    platform_sprites.update()
    active_sprite.update()

    # Draw / Render
    screen.fill(BLACK)
    platform_sprites.draw(screen)
    active_sprite.draw(screen)
    draw_heart(screen, sprite_sheet, player.life)

    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
