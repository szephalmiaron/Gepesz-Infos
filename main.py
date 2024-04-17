import pygame
from level import Level
from settings import WIDTH, HEIGHT, level_map_1, level_choice
from player import Gepesz
from infos import Infos
from enemy import Enemy
from events import event_death, event_home, event_pause, event_restart, event_unpause
from timer import Scorer, Timer


pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))


infos = Infos((int(WIDTH / 2), int(HEIGHT / 2 - 50)))
gepesz = Gepesz((int(WIDTH / 2), int(HEIGHT / 2)))
enemy = Enemy((int(WIDTH / 2), int(HEIGHT / 2)))
game_font: pygame.font.Font = pygame.font.Font(None, 60)
game_font_2: pygame.font.Font = pygame.font.Font(None, 35)




SPEED = 5


clock = pygame.time.Clock()
timer = Timer(screen, game_font, (500, 100, 200, 100), clock)
scorer = Scorer(screen, game_font, (300, 100, 200, 100))
level = Level(screen, infos, gepesz, enemy, game_font, timer, scorer)

background: pygame.Surface = pygame.image.load(level.background_image).convert()
past_level = level.current_level

running = True
paused: bool = False
alive: bool = True
iterrated: bool = False
while running:
    if level.current_level != past_level:
        background = pygame.image.load(level.background_image).convert()
        past_level = level.current_level
    level.screen_fill(screen, background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
            paused = False
            alive = True
            level.home()


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
    elif level.game_finished:
        level.endmenu()
        screen.blit((game_font.render("Gratulálok!", True, (0, 0, 0))), ((WIDTH / 2) - 60, HEIGHT / 2 -150))
        screen.blit((game_font.render("Sikeresen kijátszottátok a játékot!", True, (0, 0, 0))), ((WIDTH / 2) - 260, (HEIGHT / 2) - 100))
    elif not paused and alive:
        level.run()


    iterrated = False
    pygame.display.update()
    clock.tick_busy_loop(60)
