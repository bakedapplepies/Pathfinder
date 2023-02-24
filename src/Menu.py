import pygame
import sys

from Window import Window
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
        self.transparent_background.set_alpha(190)
        self.transparent_background.fill(GREY)
        
        # widgets
        self.settings_label = TextBox(self.window, "Settings", 96, (RESOLUTION[0]/10, RESOLUTION[1]/6))
        self.BFS_delay: str = "Off"
        self.BFS_delay_label = TextBox(self.window, f"Enable BFS delay: {self.BFS_delay}", 36, (self.settings_label.pos[0] + 10, self.settings_label.pos[1] + 110))
    
    # INPUTS
    def PollInput(self):
        keydown = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.BFS_delay_label.text_box.collidepoint(pygame.mouse.get_pos()):  # get Rect
                if self.BFS_delay == "On":
                    self.BFS_delay = "Off"
                elif self.BFS_delay == "Off":
                    self.BFS_delay = "On"
                print(self.BFS_delay)
                self.BFS_delay_label.setText(f"Enable BFS delay: {self.BFS_delay}")
            elif event.type == pygame.KEYDOWN:
                keydown = True
            # print(self.BFS_delay_label.text_box.get_rect())

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] and keydown:
            self.window.paused = False
            self.window.sceneManager.switchScene(Scenes.Pathfinder)
    
    # RENDERING
    def Render(self):
        self.window.sceneManager.pathfinder.DrawGrid()
        self.pygame_window.blit(self.transparent_background, (0, 0))
        # self.pygame_window.blit(self.BFS_delay_label, self.BFS_delay_label.pos)
        self.settings_label.Render()
        self.BFS_delay_label.Render()
    