import pygame

class Timer():
    current_time = 0
    def __init__(self, surface, font, rect):
        self.surface = surface
        self.font = font
        self.timer_rect = rect

    def time_print(self):
        self.current_time = int(pygame.time.get_ticks() / 1000)
        self.surface.blit((self.font.render(f"Eltelt idő: {self.current_time}", True, (0, 0, 0))), self.timer_rect)
    
    def reset_timer(self):
        self.current_time -= self.current_time