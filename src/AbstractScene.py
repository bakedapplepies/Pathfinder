import pygame

from main import Window


class AbstractScene:
    def __init__(self):
        self.window: Window = None
        self.pygame_window: pygame.Surface = None
    
    def PollInput(self):
        pass
    
    def Render(self):
        pass
    
    def LoadScene(self):
        pass
    