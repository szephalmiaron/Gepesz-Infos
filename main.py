import pygame
from level import Level
from settings import WIDTH, HEIGHT, level_map_1, level_choice
from player import Gepesz
from infos import Infos
from enemy import Cigany
from events import *


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

infos = Infos((WIDTH / 2, HEIGHT / 2 - 50))  
gepesz = Gepesz((WIDTH / 2, HEIGHT / 2))
cigany = Cigany((WIDTH / 2, HEIGHT / 2))



SPEED = 5


clock = pygame.time.Clock()
level = Level(screen, infos, gepesz, cigany)
mouse_data_store = MouseDataStore()
BACKGROUND = pygame.image.load(level.background_image).convert() 

RUNNING = True
paused: bool = False
alive: bool = True
iterrated: bool = False
while RUNNING:    
    screen.blit(BACKGROUND, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  
            if not paused:
                paused = True
                iterrated = True
            if paused and not iterrated:
                paused = False
        if event.type == event_restart:
            level = Level(screen, infos, gepesz, cigany)
    mouse_position = pygame.mouse.get_pos()
    mouse_data_store.getmousepos(mouse_position)
    print(mouse_data_store.mouse_pos)
     
    level.run(paused, alive)
    iterrated = False
    pygame.display.update()
    clock.tick(60)
