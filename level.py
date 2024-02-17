import pygame
from tiles import Tile
from settings import tile_size

class Level:
    def __init__(self, level_data, surface, infos, gepesz):
        self.display_surface = surface
        self.tiles_dict = {}
        self.players = pygame.sprite.Group()  # Use a regular Group for multiple players
        self.infos = infos  # Store Infos instance
        self.gepesz = gepesz  # Store Gepesz instance
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for coll_index, cell in enumerate(row):
                if cell == "S":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    tile_X = Tile((x, y))
                    self.tiles.add(tile_X)  
                elif cell == "I":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.infos.rect.topleft = (x, y)  # Set position of Infos
                    self.players.add(self.infos)  # Add Infos to player group
                elif cell == "G":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.gepesz.rect.topleft = (x, y)  # Set position of Gepesz
                    self.players.add(self.gepesz)  # Add Gepesz to player group

    def run(self):
        self.tiles.draw(self.display_surface)
        self.players.update()  # Update all players
        self.players.draw(self.display_surface)  # Draw all players
        self.horizontal_collision()
        self.vertical_collision()

    def horizontal_collision(self):
        for player in self.players:
            player.rect.x += player.direction.x * player.speed

            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left

    def vertical_collision(self):
        for player in self.players:
            player.apply_gravity()

            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.y > 0:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0
                        player.on_ground = True
                    elif player.direction.y < 0:
                        player.rect.top = sprite.rect.bottom
                        player.direction.y = 0
                        player.on_ceiling = True
        
        for player in self.players:
            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling = False

