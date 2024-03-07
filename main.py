import pygame
from level import Level
from settings import WIDTH, HEIGHT, level_map_1, level_choice
from player import Gepesz
from infos import Infos
from enemy import Cigany


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

infos = Infos((WIDTH / 2, HEIGHT / 2 - 50))  
gepesz = Gepesz((WIDTH / 2, HEIGHT / 2))
cigany = Cigany((WIDTH / 2, HEIGHT / 2))

background_image: str = "graphics/map/jedlik_epulet.png"

BACKGROUND = pygame.image.load(background_image) 
SPEED = 5

current_level: str = level_map_1


clock = pygame.time.Clock()
level = Level(current_level, screen, infos, gepesz, cigany)

RUNNING = True
paused: bool = False
alive: bool = True
while RUNNING and alive:
    screen.blit(BACKGROUND, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            level.menu(screen)
            paused = True

    if not paused:    
        infos.update()  
        alive = level.run()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
