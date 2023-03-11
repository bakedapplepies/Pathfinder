import pygame
import sys
import json

from main import Window
from AbstractScene import AbstractScene
from TextBox import TextBox
from constants import *


"""
    GUI for controlling the Pathfinder window
"""
class Menu(AbstractScene):
    def __init__(self, window: Window):
        # window
        self.window = window
        self.pygame_window = window.pygame_window
        
        self.transparent_background = pygame.Surface(RESOLUTION)
        self.transparent_background.set_alpha(240)
        self.transparent_background.fill(Color.GREY)
        
        # load settings
        with open("config/settings.json") as datafile:
            self.settingsData = json.load(datafile)
        
        # widgets
        self.settings_label = TextBox(self.window, "Settings", 96, (RESOLUTION[0]/10, RESOLUTION[1]/6))
        
        self.delay: str = self.settingsData["delay"]
        self.delay_label = TextBox(self.window, f"Enable delay: {self.delay}", 36, (self.settings_label.pos[0] + 10, self.settings_label.pos[1] + 110))
    
        self.mouse_mode: str = self.settingsData["mouse_mode"]
        self.mouse_mode_label = TextBox(self.window, f"Mouse mode: {self.mouse_mode}", 36, (self.delay_label.pos[0], self.delay_label.pos[1] + 60))
    
        self.algorithm: str = self.settingsData["algorithm"]
        self.algorithm_label = TextBox(self.window, f"Algorithm: {self.algorithm}", 36, (self.delay_label.pos[0], self.mouse_mode_label.pos[1] + 60))
    
    def __del__(self):
        # rewrite to json
        with open("config/settings.json", "w") as datafile:
            json.dump(self.settingsData, datafile, indent=4)
        
    # INPUTS
    def PollInput(self):
        keydown = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.window.saveloadManager.save("ColorGrid", self.window.sceneManager.pathfinder.grid.colorGrid)
                pygame.quit()
                sys.exit()
                
            # delay label
            elif event.type == pygame.MOUSEBUTTONDOWN and self.delay_label.text_box.collidepoint(pygame.mouse.get_pos()):  # get Rect
                if self.delay == "On":
                    self.delay = "Off"
                    self.settingsData["delay"] = "Off"
                elif self.delay == "Off":
                    self.delay = "On"
                    self.settingsData["delay"] = "On"
                self.delay_label.setText(f"Enable delay: {self.delay}")
                
            # mouse mode label 
            elif event.type == pygame.MOUSEBUTTONDOWN and self.mouse_mode_label.text_box.collidepoint(pygame.mouse.get_pos()):
                if self.mouse_mode == "Trackpad":
                    self.mouse_mode = "Mouse"
                    self.settingsData["mouse_mode"] = self.mouse_mode
                elif self.mouse_mode == "Mouse":
                    self.mouse_mode = "Trackpad"
                    self.settingsData["mouse_mode"] = self.mouse_mode
                self.mouse_mode_label.setText(f"Mouse mode: {self.mouse_mode}")
            
            # algorithm label
            elif event.type == pygame.MOUSEBUTTONDOWN and self.algorithm_label.text_box.collidepoint(pygame.mouse.get_pos()):
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
            self.window.sceneManager.pathfinder.Render()
            self.window.sceneManager.switchScene(Scenes.PATHFINDER)
    
    # RENDERING
    def Render(self):
        self.window.sceneManager.pathfinder.DrawGrid()
        self.pygame_window.blit(self.transparent_background, (0, 0))
        
        # render text
        self.settings_label.Render()
        self.delay_label.Render()
        self.mouse_mode_label.Render()
        self.algorithm_label.Render()
    