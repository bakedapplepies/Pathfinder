import pygame
import time
import ctypes
import sys
import subprocess
import pkg_resources
# import profile

import SceneManager
from SaveLoadManager import SaveLoadManager
from constants import *


class Window(pygame.Surface):
    def __init__(self):
        # Main window
        pygame.Surface.__init__(self, RESOLUTION)
        
        pygame.display.set_caption("Pathfinder")
        self.pygame_window: pygame.Surface = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE)

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("pathfinder.johnbach")
        icon = pygame.image.load("resources/icons/32_pathfinder_icon.png").convert()
        pygame.display.set_icon(icon)
        
        # Window variables
        self.clock = pygame.time.Clock()

        self.running: bool = True
        self.paused: bool = False
        self.begin: float = None
        self.deltaTime: float = None
        self.totalTimePerSec: float = 0.0
        self.windowFPS: int = 0
        
        # State saving Manager
        self.saveloadManager = SaveLoadManager(dir="save_data", extension=".dat")
        
        # Scene Manager
        self.sceneManager = SceneManager.SceneManager(window=self)
        self.sceneManager.pathfinder.resetExploredNodes()

    def showFPS(self):
        if self.deltaTime != 0: pygame.display.set_caption(f"Pathfinder - FPS: {self.windowFPS}")

    def calculateDeltaTime(self):
        self.deltaTime = time.time() - self.begin
        self.begin = time.time()
        self.calculateAndShowFPS()
        
    def calculateAndShowFPS(self):
        self.windowFPS += 1
        self.totalTimePerSec += self.deltaTime
        if self.totalTimePerSec >= 1.0:
            self.showFPS()
            self.totalTimePerSec = 0
            self.windowFPS = 0
        
    def Loop(self):
        self.deltaTime = 0.0
        self.begin = 0.0
        
        while self.running:
            self.calculateDeltaTime()
            
            self.sceneManager.PollInput()
            
            self.sceneManager.Render()
            
            # self.gui.mainloop()
            self.blit(self.pygame_window, (0, 0))
            pygame.display.update()
            # self.clock.tick(FPS)
    
def checkDependencies() -> None:
    required = { "pygame", "pillow" }
    installed = { pkg.key for pkg in pkg_resources.working_set }
    missing = required - installed
    
    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)


if __name__ == "__main__":
    # checkDependencies()
    pygame.init()
    
    window = Window()
    window.Loop()
