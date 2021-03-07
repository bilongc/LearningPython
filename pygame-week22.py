import pygame
import random
from os import path

img_dir = path.join(path.dirname(__file__), 'img')
sound_dir = path.join(path.dirname(__file__), 'sound')

WIDTH = 360
HEIGHT = 480
FPS = 30
BLOCK_X = 50
BLOCK_Y = 40
MOB_X = 30
MOB_Y = 20
BULLET_X = 10
BULLET_Y = 20

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shmup")
clock = pygame.time.Clock()

background = pygame.image.load(path.join(img_dir, 'starfield.png')).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, 'playerShip1_orange.png')).convert()
mob_img = pygame.image.load(path.join(img_dir, 'meteorBrown_med1.png')).convert()
bullet_img = pygame.image.load(path.join(img_dir, 'laserRed16.png')).convert()
shoot_sound = pygame.mixer.Sound(path.join(sound_dir, 'shoot.wav'))
background_sound = pygame.mixer.Sound(path.join(sound_dir, 'background.wav'))

explosion = [ ]

for i in range(9):
    filename = 'regularExplosion0' + str(i) + '.png'
    expl_img = pygame.image.load(path.join(img_dir, filename)).convert()
    expl_img.set_colorkey(BLACK)
    explosion.append(expl_img)

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = explosion[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame_id = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame_id += 1
            if self.frame_id == len(explosion):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion[self.frame_id]
                self.rect = self.image.get_rect()
                self.rect.center = center

# Game loop
# Event processing
# When quit is clicked, what to do?
# When mouse is clicked, what to do?
# When keyboard is pressed, what to do?
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
#        self.image = pygame.Surface((BLOCK_X, BLOCK_Y))
#        self.image.fill(GREEN)
        self.image = pygame.transform.scale(player_img, (BLOCK_X, BLOCK_Y))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x -= 8
        if keystate[pygame.K_RIGHT]:
            self.rect.x += 8
        if keystate[pygame.K_SPACE]:
            self.shoot()
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.right > WIDTH:
            self.rect.x = WIDTH - BLOCK_X

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = Bullet(self.rect.centerx, self.rect.y)
            sprites.add(bullet)
            bullets.add(bullet)
            shoot_sound.play()

# Define Mob sprite
class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
#        self.image = pygame.Surface((MOB_X, MOB_Y))
#        self.image.fill(RED)
        self.scale = random.randint(10, 100) / 100 
        self.image = pygame.transform.scale(mob_img, (int(MOB_X * self.scale), int(MOB_X * self.scale)));
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH)
        self.rect.y = random.randint(-100, -10)
        self.speedy = random.randint(1, 5)
        self.speedx = random.randint(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.y > HEIGHT or self.rect.x > WIDTH or self.rect.x < 0:
            self.rect.y = random.randint(-100, -10)
            self.rect.x = random.randint(0, WIDTH)
            self.speedy = random.randint(1, 5)
            self.speedx = random.randint(-3, 3)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed

        if (self.rect.y < 0):
            self.kill()

player = Player()
sprites = pygame.sprite.Group()
sprites.add(player)
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
for i in range(10):
    m = Mob()
    sprites.add(m)
    mobs.add(m)

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, False, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

running = True
score = 0
background_sound.set_volume(0)
background_sound.play(-1)
while running:
    clock.tick(FPS)

    # Check events
    for event in pygame.event.get():
        # Check for closing window event
        if event.type == pygame.QUIT:
            running = False
#        elif event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_SPACE:
#                player.shoot()

    # Update
    sprites.update()

    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        running = False

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for h in hits:
        m = Mob()
        sprites.add(m)
        mobs.add(m)
        score += int((1 - h.scale) * 10)
        expl = Explosion(h.rect.center)
        sprites.add(expl)

    # Draw / Render
    screen.blit(background, background_rect)
    sprites.draw(screen)
    draw_text(screen, str(score), 16, WIDTH/2, 10)

    # After drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
