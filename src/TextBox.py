import pygame

from main import Window
from constants import *

class TextBox(pygame.Surface):
    def __init__(self, window: Window, text: str, size: int, pos: tuple):
        # window details
        self.window = window
        self.pos = pos

        self.my_font: pygame.font.Font = pygame.font.SysFont("Bahnschrift", size)
        self.text_surface = self.my_font.render(text, True, Color.WHITE, None)
        
    def Render(self):
        self.window.pygame_window.blit(self.text_surface, self.pos)

    def setText(self, text: str):
        self.text_surface = self.my_font.render(text, True, Color.WHITE, None)  # text, antialias, color
        self.window.sceneManager.LoadScene()
        
    def getTextBox(self) -> pygame.Rect:
        return self.text_surface.get_rect(topleft=self.pos)
