import pygame
import sys
from pygame.locals import *

# Colors
bgColor = (219, 244, 255)
sideBarColor = (255, 221, 217)
sideBarBorder = (201, 135, 127)
white = (255, 255, 255)
pink = (245, 91, 175)
darkBlue = (40, 55, 79)
fadedRed = (156, 89, 104)

class TextInput:
    def __init__(self, x, y, width, height, font, initial_text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = white
        self.text = initial_text
        self.font = font
        self.txt_surface = self.font.render(self.text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input box
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = pink if self.active else white

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                    self.color = white
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def get_value(self):
        try:
            return int(self.text)
        except ValueError:
            return 0
