import pygame
from settings import WIDTH, HEIGHT
from tiles import Button
from events import *

class Menu_Buttons(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], buttontype):
        super().__init__()
        if buttontype == "home":
            self.image = pygame.image.load("graphics/buttons/homgomboooo.png").convert_alpha()
        elif buttontype == "restart":
            self.image = pygame.image.load("graphics/buttons/restart_button.png").convert_alpha()
        elif buttontype == "quit":
            self.image = pygame.image.load("graphics/buttons/quit_button.png").convert_alpha()
        elif buttontype == "resume":
            self.image = pygame.image.load("graphics/buttons/resume_button.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.type_str = buttontype
class Menu:
    POS_1_3 = (HEIGHT/4)
    POS_2_3 = (HEIGHT/4)*2
    POS_3_3 = (HEIGHT/4)*3
    POS_1_2 = (HEIGHT/3)
    POS_2_2 = (HEIGHT/3)*2
    POS_1_4 = (HEIGHT/5)
    POS_2_4 = (HEIGHT/5)*2
    POS_3_4 = (HEIGHT/5)*3
    POS_4_4 = (HEIGHT/5)*4
    background_image = "graphics\map\crackhead.png"

    def __init__(self, screen):
        self.screen = screen
        self.all_buttons: list[Button] = pygame.sprite.Group()


    def checkcollision(self):
        for button in self.all_buttons:
            if button.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed() == (True, False, False):
                if button.type_str == "home":
                    pygame.event.post(pygame.event.Event(event_home)) 
                if button.type_str == "resume":
                    pygame.event.post(pygame.event.Event(event_unpause))
                if button.type_str == "quit":
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                if button.type_str == "restart":
                    pygame.event.post(pygame.event.Event(event_restart))
    
    def pausemenu(self):
        self.screen.fill((0, 255, 0))
        home_button = Menu_Buttons((WIDTH//2, self.POS_1_4), "home")
        self.all_buttons.add(home_button)
        restart_button = Menu_Buttons((WIDTH//2, self.POS_2_4), "restart")
        self.all_buttons.add(restart_button)
        quit_button = Menu_Buttons((WIDTH//2, self.POS_3_4), "quit")
        self.all_buttons.add(quit_button)
        resume_button = Menu_Buttons((WIDTH//2, self.POS_4_4), "resume")
        self.all_buttons.add(resume_button)

        self.all_buttons.draw(self.screen)
        self.checkcollision()
    
    def deathmenu(self):
        self.screen.fill((255, 0, 0,))
        home_button = Menu_Buttons((WIDTH//2, self.POS_1_3), "home")
        self.all_buttons.add(home_button)
        restart_button = Menu_Buttons((WIDTH//2, self.POS_2_3), "restart")
        self.all_buttons.add(restart_button)
        quit_button = Menu_Buttons((WIDTH//2, self.POS_3_3), "quit")
        self.all_buttons.add(quit_button)

        self.all_buttons.draw(self.screen)
        self.checkcollision()
    
    def endmenu(self):
        self.screen.fill((0,0,255))
        quit_button = Menu_Buttons((WIDTH//2, self.POS_2_3), "quit")
        self.all_buttons.add(quit_button)
        self.all_buttons.draw(self.screen)
        self.checkcollision()

    def menudraw(self, menutype):
        if menutype == "pause":
            self.pausemenu()
        elif menutype == "death":
            self.deathmenu()
        elif menutype == "end":
            self.endmenu()

    def delete_all(self):
        for button in self.all_buttons:
            self.all_buttons.remove(button)