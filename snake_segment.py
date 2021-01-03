import pygame
import pygame.sprite

from pygame import Color
from pygame.sprite import Sprite

class SnakeSegment(Sprite):

    def __init__(self, x, y, width, color):
        super().__init__()
        self.color = color

        self.image = pygame.Surface([width, width])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        return 