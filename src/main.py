import pygame
from pygame.locals import *
import time
import ctypes
import sys
import subprocess
import pkg_resources
import cProfile
import os
import json
# import profile

import SceneManager
from SaveLoadManager import SaveLoadManager
from constants import *


class Window(pygame.Surface):
    def __init__(self):
        # Main window
        pygame.Surface.__init__(self, RESOLUTION)
        
        pygame.display.set_caption("Pathfinder")
        flags = DOUBLEBUF | VIDEORESIZE
        self.pygame_window: pygame.Surface = pygame.display.set_mode(RESOLUTION, flags, 64)
        

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("pathfinder.johnbach")
        icon = pygame.image.load("resources/icons/32_pathfinder_icon.png").convert()
        pygame.display.set_icon(icon)
        
        # event handler config
        pygame.event.set_allowed([
            pygame.QUIT,
            pygame.KEYDOWN,
            pygame.MOUSEBUTTONDOWN,
            pygame.VIDEORESIZE
        ])
        
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
            
            self.blit(self.pygame_window, (0, 0))
            pygame.display.flip()
            
    
def checkDependencies() -> None:
    required = { "pygame", "pillow" }
    installed = { pkg.key for pkg in pkg_resources.working_set }
    missing = required - installed
    
    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

def main(profile: bool = False):
    with open("config/settings.json") as datafile:
        data = json.load(datafile)
        if data["profile"]: profile = True
    
    if not os.path.exists("logs"): os.mkdir("logs")
    if profile:
        with open("logs/profile.log", "w") as sys.stdout:
            cProfile.run("pathfind()", sort="tottime")
    else:
        pathfind()

def pathfind():
    # checkDependencies()
    pygame.init()
    
    window = Window()
    window.Loop()
    

if __name__ == "__main__":
    main()
