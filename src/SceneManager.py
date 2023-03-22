import pygame

from AbstractScene import AbstractScene
from main import Window
from Menu import Menu
from Pathfinder import Pathfinder
from constants import *


# Also responsible for calculating the to-be-updated area
class SceneManager(AbstractScene):
    def __init__(self, window: Window):
        self.update_rectangles: list = list()
        
        # Where scenes initializations are called
        self.scene = Scenes.PATHFINDER
        self.pathfinder = Pathfinder(window=window)
        self.menu = Menu(window=window)
        
        self.scenes = {
            Scenes.PATHFINDER: self.pathfinder,
            Scenes.MENU: self.menu,
        }
        
    def SwitchScene(self, sceneName) -> None:
        self.scene = sceneName
        self.LoadScene()
        
    def LoadScene(self):
        self.scenes[self.scene].LoadScene()
        pygame.display.update()
        
    def addUpdateRect(self, rect: pygame.Rect):
        self.update_rectangles.append(rect)
        
    def PollInput(self):
        """Poll Inputs and get to-be-updated areas/rects for Render method"""
        self.update_rectangles = list()
        self.scenes[self.scene].PollInput()
        
    def Render(self):
        """Update screen using rects"""
        for rectangle in self.update_rectangles:
            pygame.display.update(rectangle)
                    