import pygame
from level import Level
from settings import WIDTH, HEIGHT, level_map
from player import Gepesz
from infos import Infos
from enemy import Cigany


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

infos = Infos((WIDTH / 2, HEIGHT / 2 - 50))  
gepesz = Gepesz((WIDTH / 2, HEIGHT / 2))
cigany = Cigany((WIDTH / 2, HEIGHT / 2))

BACKGROUND = (135, 206, 235)
SPEED = 5

clock = pygame.time.Clock()
level = Level(level_map, screen, infos, gepesz, cigany)

RUNNING = True
paused: bool = False
alive: bool = True
while RUNNING and alive:
    screen.fill(BACKGROUND)
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
