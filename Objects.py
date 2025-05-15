import pygame

class Player(pygame.sprite.Sprite):
    position = pygame.Vector2(160,480)
    posX = 160
    posY = 480
    health = 3
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((80,80))
        self.image.fill('blue')
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posX,self.posY)

class Goblin(pygame.sprite.Sprite):
    position = pygame.Vector2(0,0)
    posX = 0
    posY = 0
    health = 1
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((80,80))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posX,self.posY)
    enemy_ID = 1

class Wall_Tile(pygame.sprite.Sprite):
    position = pygame.Vector2(0,0)
    posX = 0
    posY = 0
    def __init__(self,tilepos_x,tilepos_y):
        super().__init__()
        self.image = pygame.Surface((80,80))
        self.image.fill('gray')
        self.rect = self.image.get_rect()
        self.rect.topleft = (tilepos_x,tilepos_y)

class Floor_Tile(pygame.sprite.Sprite):
    position = pygame.Vector2(0,0)
    posX = 0
    posY = 0
    def __init__(self,tilepos_x,tilepos_y):
        super().__init__()
        self.image = pygame.Surface((80,80))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.topleft = (tilepos_x,tilepos_y)