from typing import List
import pygame

class Gepesz(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__()

        self.image = pygame.image.load("graphics/characters/gepesz/gepeszanimacio2(default).png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.frame_index: float = 0
        self.direction = pygame.math.Vector2(0, 0)
        self.speed: int = 5
        self.gravity: float = 0.6
        self.jump_speed: float = -14
        self.facing_left: bool = True
        self.on_ground: bool = False
        self.on_ceiling: bool = False
        self.on_left: bool = False
        self.on_right: bool = False
        
    def get_input(self) -> None:
        keys: List[bool] = pygame.key.get_pressed()
        image_path = "graphics/characters/gepesz/gepeszanimacio2(default).png"
        if keys[pygame.K_d]:
            self.direction.x = 1
            self.facing_left = False
            loaded_image_1 = pygame.image.load(image_path)
            converted_image_1 = loaded_image_1.convert_alpha()
            self.image = loaded_image_1
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.facing_left = True
            loaded_image_1 = pygame.image.load(image_path)
            converted_image_1 = loaded_image_1.convert_alpha()
            flipped_image_1 = pygame.transform.flip(converted_image_1, True, False)
            self.image = flipped_image_1
        else:
            self.direction.x = 0

        if keys[pygame.K_w] and self.on_ground:
            self.jump()

    def apply_gravity(self) -> None:
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self) -> None:
        self.direction.y = self.jump_speed

    def update(self) -> None:
        self.get_input()

    def save_original_pos(self, pos: tuple[int, int]):
        self.original_pos: tuple[int, int] = pos