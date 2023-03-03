import pygame

from Window import Window
from constants import *

class TextBox(pygame.Surface):
    def __init__(self, window: Window, string: str, size: int, pos: tuple):
        # window details
        super().__init__(pos)
        self.window = window
        self.pos = pos

        self.my_font: pygame.font.Font = pygame.font.SysFont("Bahnschrift", size)
        self.text_surface = self.my_font.render(string, True, Color.WHITE)
        self.text_surface.set_alpha(255)

        self.text_box = self.text_surface.get_rect(topleft=pos)

    def Render(self):
        self.window.pygame_window.blit(self.text_surface, self.pos)

    def setPos(self, newPos: tuple):
        self.pos = newPos

    def setText(self, text: str):
        self.text_surface = self.my_font.render(text, True, Color.WHITE)
