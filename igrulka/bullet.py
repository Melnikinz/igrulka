import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    self.y -= self.speed_factor
    self.rect.y = self.y
def draw_bullet(self):
    pygame.draw.rect(self.screen, self.color, self.rect)