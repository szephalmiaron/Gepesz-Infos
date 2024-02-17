import pygame
from settings import SPEED

SPEED 

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, start_pos):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=start_pos)

    def update(self, keys):
        if keys[self.key_right] and self.rect.right <= self.screen_width:
            self.rect.x += SPEED
        elif keys[self.key_left] and self.rect.left >= 0:
            self.rect.x -= SPEED
        if keys[self.key_up] and self.rect.top >= 0:
            self.rect.y -= SPEED
        elif keys[self.key_down] and self.rect.bottom <= self.screen_height:
            self.rect.y += SPEED
