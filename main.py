import pygame
from os import path

imageDir = path_img = path.join(path.dirname(__file__), "img")

WIDTH = 1000
HEIGHT = 500
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platoon")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

cube_color_text = "белый"
cube_color = WHITE

def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(pygame.font.match_font("arial"), size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.model = pygame.Surface((50, 50))
        self.model.fill(RED)
        self.vector = None
        self.image = self.model
        self.rect = self.model.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
    def update(self):
        if self.rect.left <= 0:
            self.rect.x = 0
        if self.rect.top <= 0:
            self.rect.y = 0
        if self.rect.right >= WIDTH:
            self.rect.x = WIDTH - 50
        if self.rect.bottom >= HEIGHT:
            self.rect.y = HEIGHT - 50

class Cube(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        self.model = pygame.Surface((50, 50))
        self.model.fill(color)
        self.image = self.model
        self.rect = self.model.get_rect()
        self.rect.center = (x, y)
    def update(self):
        if self.rect.left <= 0:
            return 0
        if self.rect.top <= 0:
            return 0
        if self.rect.right >= WIDTH:
            return 0
        if self.rect.bottom >= HEIGHT:
            return 0



player = Player()

all_sprites = pygame.sprite.Group()

all_sprites.add(player)


run = True
while run:
    clock.tick(FPS)
    screen.fill(BLACK)
    draw_text(screen, "Цвет куба : " + cube_color_text, 18, WIDTH//4, HEIGHT//16)
    all_sprites.update()
    all_sprites.draw(screen)
    print(player.vector)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.rect.y -= 50
                player.vector = "up"
            if event.key == pygame.K_s:
                player.rect.y += 50
                player.vector = "down"
            if event.key == pygame.K_a:
                player.rect.x -= 50
                player.vector = "left"
            if event.key == pygame.K_d:
                player.rect.x += 50
                player.vector = "right"
            if event.key == pygame.K_1:
                cube_color_text = "синий"
                cube_color = BLUE
            if event.key == pygame.K_2:
                cube_color_text = "зеленый"
                cube_color = GREEN
            if event.key == pygame.K_3:
                cube_color_text = "белый"
                cube_color = WHITE
            if event.key == pygame.K_SPACE:
                if player.vector == "up":
                    cube = Cube(player.rect.x + 25, player.rect.y - 25, cube_color)
                    all_sprites.add(cube)
                    all_sprites.draw(screen)
                if player.vector == "down":
                    cube = Cube(player.rect.x + 25, player.rect.bottom + 25, cube_color)
                    all_sprites.add(cube)
                    all_sprites.draw(screen)
                if player.vector == "right":
                    cube = Cube(player.rect.right + 25, player.rect.y + 25, cube_color)
                    all_sprites.add(cube)
                    all_sprites.draw(screen)
                if player.vector == "left":
                    cube = Cube(player.rect.left - 25, player.rect.y + 25, cube_color)
                    all_sprites.add(cube)
                    all_sprites.draw(screen)
            
    pygame.display.update()
    pygame.display.flip()