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

BACKGROUND = pygame.image.load(level.background_image).convert()
past_level = level.current_level 

RUNNING = True
paused: bool = False
alive: bool = True
iterrated: bool = False
while RUNNING:
    if level.current_level != past_level:  
        BACKGROUND = pygame.image.load(level.background_image).convert()
        past_level = level.current_level 
    level.screen_fill(screen, BACKGROUND)

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
            level.level_reset()
            alive = True
            paused = False
        if event.type == event_pause:
            paused = True
        if event.type == event_unpause:
            paused = False
        if event.type == event_death:
            alive = False

    if paused:
        level.pausemenu()
    elif not alive:
        level.deathmenu()
    elif not paused and alive:
        level.run()

    
    iterrated = False
    pygame.display.update()
    clock.tick(60)
