import pygame

from Window import Window
from AbstractScene import AbstractScene
from Pathfinder import Pathfinder
from Menu import Menu


class SceneManager(AbstractScene):
    def __init__(self, window: Window):
        self.scene = "Pathfinder"
        self.pathfinder = Pathfinder(window=window)
        self.menu = Menu(window=window)
        
        self.scenes = {
            "Pathfinder": self.pathfinder,
            "Menu": self.menu,
        }
        
    def switchScene(self, sceneName: str) -> None:
        self.scene = sceneName
        
    def PollInput(self):
        self.scenes[self.scene].PollInput()
        
    def Render(self):
        self.scenes[self.scene].Render()