import pygame
from settings import WIDTH, HEIGHT

class Menu_Buttons(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], buttontype):
        super().__init__()
        if buttontype == "restart":
            self.image = pygame.image.load("graphics/buttons/restart_button.png")
        elif buttontype == "quit":
            self.image = pygame.image.load("graphics/buttons/quit_button.png")
        elif buttontype == "resume":
            self.image = pygame.image.load("graphics/buttons/resume_button.png")
        self.rect = self.image.get_rect(topleft = pos)
class Menu:
    POS_1_3 = (HEIGHT/4)
    POS_2_3 = (HEIGHT/4)*2
    POS_3_3 = (HEIGHT/4)*3
    POS_1_2 = (HEIGHT/3)
    POS_2_2 = (HEIGHT/3)*2

    def __init__(self, screen):
        self.screen = screen
        self.all_buttons = pygame.sprite.Group()
    
    def pausemenu(self):
        self.screen.fill((0, 255, 0))
        restart_button = Menu_Buttons((WIDTH//2, self.POS_1_3), "restart")
        self.all_buttons.add(restart_button)
        quit_button = Menu_Buttons((WIDTH//2, self.POS_2_3), "quit")
        self.all_buttons.add(quit_button)
        resume_button = Menu_Buttons((WIDTH//2, self.POS_3_3), "resume")
        self.all_buttons.add(resume_button)

        self.all_buttons.draw(self.screen)
        self.all_buttons.remove(restart_button)
        self.all_buttons.remove(quit_button)
        self.all_buttons.remove(resume_button)
    
    def deathmenu(self):
        self.screen.fill((255, 0, 0,))

        restart_button = Menu_Buttons((WIDTH//2, self.POS_1_2), "restart")
        self.all_buttons.add(restart_button)
        quit_button = Menu_Buttons((WIDTH//2, self.POS_2_2), "quit")
        self.all_buttons.add(quit_button)

        self.all_buttons.draw(self.screen)
        self.all_buttons.remove(restart_button)
        self.all_buttons.remove(quit_button)
    
    def menudraw(self, menutype):
        if menutype == "pause":
            self.pausemenu()
        elif menutype == "death":
            self.deathmenu()