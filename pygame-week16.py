import pygame

print("Initialization")
pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.update()

# Game loop
# Event processing
# When quit is clicked, what to do?
# When mouse is clicked, what to do?
# When keyboard is pressed, what to do?
# RGB: Red - Green - Blue
# Each color component has 8 bit (1 byte) to represent that component
# Each component value can be between 0-255

FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLOCK_X = 30
BLOCK_Y = 30
SCREEN_X = 400
SCREEN_Y = 300

clock = pygame.time.Clock()

running = True

class Block(pygame.sprite.Sprite):
    def __init__(self, direction, fill_color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((BLOCK_X, BLOCK_Y))
        self.image.fill(fill_color)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_X / 2, SCREEN_Y / 2)
        self.direction = direction

    def update(self):
        if self.direction == 'LEFT':
            self.rect.x = self.rect.x - 5
        else:
            self.rect.x = self.rect.x + 5
            
        if self.rect.x > SCREEN_X:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = SCREEN_X

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))

block_left = Block('LEFT', GREEN)
block_right = Block('RIGHT', RED)

while running:
    clock.tick(FPS)
    
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    block_left.update()
    block_right.update()

    # Draw
    screen.fill(BLACK)
    block_right.draw(screen)
    block_left.draw(screen)

    # Flip
    pygame.display.flip()
    
pygame.quit()
