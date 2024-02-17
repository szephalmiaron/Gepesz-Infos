import pygame
from tiles import Tile
from settings import *
class Level:
    def __init__(
        self, level_data: list[str], surface: pygame.Surface
    ):
        self.display_surface: pygame.Surface = surface
        self.tiles_dict = {}
        self.setup_level(level_data)
        
    def setup_level(self, layout: list[str]) -> None:
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for coll_index, cell in enumerate(row):
                if cell == "S":
                    x: int = coll_index * tile_size
                    y: int = row_index * tile_size
                    tile_X: Tile = Tile((x, y))
                    self.tiles.add(tile_X)
    def run(self) -> None:
        self.tiles.draw(self.display_surface)
        self.player.update()
        self.player.draw(self.display_surface)

