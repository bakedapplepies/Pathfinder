import pygame
import sys

from AbstractScene import AbstractScene
from Window import Window
from constants import *


class Menu(AbstractScene):
    def __init__(self, window: Window):
        self.window = window
        self.pygame_window = window.pygame_window
    
    # INPUTS
    def PollInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    # RENDERING
    def Render(self):
        self.pygame_window.fill(WHITE)