import pygame
import random
from utils import SCREEN_WIDTH, SCREEN_HEIGHT, RED

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, level=1):
        super().__init__()
        import os
        
        self.level = level
        self.hp = 1
        self.is_big = False
        
        if self.level >= 5 and random.random() < 0.3:
            self.is_big = True
            self.hp = 4
            self.image = pygame.image.load(os.path.join('Sprites', 'BigEnemy.png')).convert_alpha()
            self.image = pygame.transform.scale(self.image, (65, 65)) 
        else:
            img_name = random.choice(['Enemy.png', 'Enemy2.png'])
            self.image = pygame.image.load(os.path.join('Sprites', img_name)).convert_alpha()
            self.image = pygame.transform.scale(self.image, (39, 39))
            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0 

    def update(self):
        self.rect.x += self.speed_x
