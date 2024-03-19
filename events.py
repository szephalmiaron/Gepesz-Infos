import pygame

event_pause = pygame.USEREVENT + 1
event_unpause = pygame.USEREVENT + 2
event_death = pygame.USEREVENT + 3
event_gamebutton = pygame.USEREVENT + 4
event_switch_on = pygame.USEREVENT + 5
event_switch_off = pygame.USEREVENT + 6
event_restart = pygame.USEREVENT + 7


class MouseDataStore(pygame.sprite.Sprite):
    mouse_pos = ()
    mouse_x = 0
    mouse_y = 0
    clicked: bool = False
    def getmousepos(self, mouse_pos, clicked):
        self.mouse_pos = mouse_pos
        self.mouse_x, self.mouse_y = mouse_pos
        self.clicked = clicked