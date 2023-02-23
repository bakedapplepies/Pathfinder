import pygame

from AbstractScene import AbstractScene
from Window import Window
from Menu import Menu
from Pathfinder import Pathfinder
from constants import *


class SceneManager(AbstractScene):
    def __init__(self, window: Window):
        self.scene = Scenes.Pathfinder
        self.pathfinder = Pathfinder(window=window)
        self.menu = Menu(window=window)
        
        self.scenes = {
            Scenes.Pathfinder: self.pathfinder,
            Scenes.Menu: self.menu,
        }
        
    def switchScene(self, sceneName: str) -> None:
        self.scene = sceneName
        
    def PollInput(self):
        self.scenes[self.scene].PollInput()
        
    def Render(self):
        self.scenes[self.scene].Render()