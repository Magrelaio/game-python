#parte mais importante e essencial do projeto ok?
import pygame
from settings import *
from tile import Tile
from player import Player
from superdebug import debug

class Level:
    def __init__(self):
        #pegar a surface de display
        self.display_surface = pygame.display.get_surface()
        #sprite group set up
        self.visible_sprites = YCameraSortGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        #setup de sprite e fodase
        self.create_map()
        
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index,col in enumerate(row):
                x= col_index * TILESIZE
                y= row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites)
    
    def run(self):
        #atualizar e 'desenhar' no game
        self.visible_sprites.custom_draw()
        self.visible_sprites.update()
        debug(self.player.speed)
        
class YCameraSortGroup(pygame.sprite.Group):
    def __init__(self):
        
        #setup geral
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        
    def custom_draw(self):
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft + self.offset
            self.display_surface.blit(sprite.image, offset_pos)