import pygame
import sys
import json

from main import Window
from AbstractScene import AbstractScene
from TextBox import TextBox
from constants import *


class Menu(AbstractScene):
    def __init__(self, window: Window):
        # window
        self.window = window
        self.pygame_window = window.pygame_window
        
        self.transparent_background = pygame.Surface(GRID_RESOLUTION)
        self.transparent_background.set_alpha(240)
        self.transparent_background.fill(Color.GREY)
        
        # load settings
        with open("config/settings.json") as datafile:
            self.settingsData = json.load(datafile)
        
        # widgets
        self.settings_label = TextBox(self.window, "Settings", 96, (GRID_RESOLUTION[0]/10, GRID_RESOLUTION[1]/6))
    
        self.mouse_mode: str = self.settingsData["mouse_mode"]
        self.mouse_mode_label = TextBox(self.window, f"Mouse mode: {self.mouse_mode}", 36, (self.settings_label.pos[0] + 10, self.settings_label.pos[1] + 110))
    
        self.algorithm: str = self.settingsData["algorithm"]
        self.algorithm_label = TextBox(self.window, f"Algorithm: {self.algorithm}", 36, (self.mouse_mode_label.pos[0], self.mouse_mode_label.pos[1] + 60))
    
    def saveSettings(self):
        # rewrite to json
        with open("config/settings.json", "w") as datafile:
            json.dump(self.settingsData, datafile, indent=4)
        
    # INPUTS
    def PollInput(self) -> None:
        keydown = False
        
        # Special Events ----------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.window.saveloadManager.save("ColorGrid", self.window.sceneManager.pathfinder.grid.colorGrid)
                self.saveSettings()
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # mouse mode label 
                if self.mouse_mode_label.getTextBox().collidepoint(pygame.mouse.get_pos()):
                    if self.mouse_mode == "Trackpad":
                        self.mouse_mode = "Mouse"
                        self.settingsData["mouse_mode"] = self.mouse_mode
                    elif self.mouse_mode == "Mouse":
                        self.mouse_mode = "Trackpad"
                        self.settingsData["mouse_mode"] = self.mouse_mode
                    self.mouse_mode_label.setText(f"Mouse mode: {self.mouse_mode}")
                
                # algorithm label
                elif self.algorithm_label.getTextBox().collidepoint(pygame.mouse.get_pos()):
                    if self.algorithm == Algorithms.BFS:
                        self.algorithm = Algorithms.DIJKSTRA
                        self.settingsData["algorithm"] = Algorithms.DIJKSTRA
                    elif self.algorithm == Algorithms.DIJKSTRA:
                        self.algorithm = Algorithms.GREEDY_BFS
                        self.settingsData["algorithm"] = Algorithms.GREEDY_BFS
                    elif self.algorithm == Algorithms.GREEDY_BFS:
                        self.algorithm = Algorithms.ASTAR
                        self.settingsData["algorithm"] = Algorithms.ASTAR
                    elif self.algorithm == Algorithms.ASTAR:
                        self.algorithm = Algorithms.BFS
                        self.settingsData["algorithm"] = Algorithms.BFS
                    self.algorithm_label.setText(f"Algorithm: {self.algorithm}")
            
            elif event.type == pygame.KEYDOWN:
                keydown = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] and keydown:
            self.window.paused = False
            self.window.sceneManager.SwitchScene(Scenes.PATHFINDER)
    
    # RENDERING
    def LoadScene(self):
        self.window.sceneManager.pathfinder.LoadScene()
        self.pygame_window.blit(self.transparent_background, (0, 0))
        
        # render text
        self.settings_label.Render()
        self.mouse_mode_label.Render()
        self.algorithm_label.Render()
    