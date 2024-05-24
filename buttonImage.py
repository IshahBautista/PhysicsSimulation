import pygame
import sys
from pygame.locals import *

class ButtonImg:
    def __init__(self, image_path, hover_image_path, x, y):
        self.image = image_path
        self.hover_image = hover_image_path
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.is_hovered = False

    def draw(self, surface):
        if self.is_hovered:
            surface.blit(self.hover_image, self.rect)
        else:
            surface.blit(self.image, self.rect)

    def is_over(self, pos):
        return self.rect.collidepoint(pos)