import pygame
from level import Level
from settings import WIDTH, HEIGHT, level_map_1, level_choice
from player import Gepesz
from infos import Infos
from enemy import Cigany
from events import *
from timer import *


pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))


infos = Infos((WIDTH / 2, HEIGHT / 2 - 50))  
gepesz = Gepesz((WIDTH / 2, HEIGHT / 2))
cigany = Cigany((WIDTH / 2, HEIGHT / 2))
game_font: pygame.font.Font = pygame.font.Font(None, 60)
game_font_2: pygame.font.Font = pygame.font.Font(None, 35)




SPEED = 5


clock = pygame.time.Clock()
timer = Timer(screen, game_font, (500, 100, 200, 100), clock)
level = Level(screen, infos, gepesz, cigany, game_font, timer)

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
        if event.type == event_home:
            level.current_level = level_choice
            level.home()
            paused = False
    
    if level.current_level == level_choice:
        screen.blit((game_font.render("A szóköz lenyomásával be tudsz menni egy ajtón", True, (0, 0, 0))), (50, 600, 50, 50))
    if level.current_level == level_map_1:
        screen.blit((game_font_2.render("A gombbal és a kapcsolóval irányítható a lift", True, (0, 0, 0))), (900, 800, 50, 50))
        screen.blit((game_font_2.render("Ha oldalról nekedjön az ellenség akkor, meghalsz", True, (0, 0, 0))), (300, 370, 50, 50))
        screen.blit((game_font_2.render("Ha ráugrassz a fejére, akkor az ellenség hal meg", True, (0, 0, 0))), (300, 400))



    if paused:
        level.pausemenu()
    elif not alive:
        level.deathmenu()
    elif not paused and alive:
        level.run()


    iterrated = False
    pygame.display.update()
    clock.tick_busy_loop(60)