import pygame
import sys

from Window import Window
from AbstractScene import AbstractScene
from constants import *


"""
    GUI for controlling the Pathfinder window
"""
class Menu(AbstractScene):
    def __init__(self, window: Window):
        # window
        self.window = window
        self.pygame_window = window.pygame_window
        
        # widgets
        # self.resume_button = pygame.Rect()
    
    # INPUTS
    def PollInput(self):
        keydown = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keydown = True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] and keydown:
            self.window.sceneManager.switchScene(Scenes.Pathfinder)
    
    # RENDERING
    def Render(self):
        self.pygame_window.fill(WHITE)