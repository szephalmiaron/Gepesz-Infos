import pygame

class Timer():
    current_time = 0
    def __init__(self, surface: pygame.Surface, font: pygame.font.Font, rect: tuple[int, int, int, int], clock: pygame.time.Clock):
        self.surface = surface
        self.font = font
        self.timer_rect = rect
        self.clock = clock

    def time_print(self):
        self.current_time += self.clock.get_time() / 1000
        self.surface.blit((self.font.render(f"Eltelt idő: {int(self.current_time)}", True, (0, 0, 0))), self.timer_rect)

    def reset_timer(self):
        self.current_time -= self.current_time

    def get_time(self):
        return self.current_time

class Scorer():
    def __init__(self, surface: pygame.Surface, font: pygame.font.Font, rect: tuple[int, int, int, int]):
        self.surface = surface
        self.font = font
        self.scorer_rect = rect
        self.score = 0

    def add_score(self, amount: int):
        self.score += amount

    def win(self, idő: int):
        if idő < 91:
            self.score += (90 - idő)

    def print_score(self):
        self.surface.blit((self.font.render(f"Pontszám: {self.score}", True, (0, 0, 0))), self.scorer_rect)
