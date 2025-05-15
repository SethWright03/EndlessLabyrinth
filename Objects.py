import pygame

class Wall_Tile(pygame.sprite.Sprite):
    position = pygame.Vector2(0,0)
    posX = 0
    posY = 0
    def __init__(self,tilepos_x,tilepos_y):
        super().__init__()
        self.image = pygame.Surface((80,80))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.topleft = (tilepos_x,tilepos_y)