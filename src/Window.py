import pygame
import time
import ctypes
import threading
import logging
import sys
import subprocess
import pkg_resources
# import profile

import SceneManager
from GUIControl import GUIControl
from constants import *


pygame.init()

class Window():
    def __init__(self):
        # Main window
        pygame.display.set_caption("Pathfinder")
        self.pygame_window: pygame.Surface = pygame.display.set_mode(RESOLUTION, pygame.RESIZABLE)

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("abc")
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
        
        # Scene Manager
        self.sceneManager = SceneManager.SceneManager(window=self)

    def showFPS(self):
        if self.deltaTime != 0: pygame.display.set_caption(f"Pathfinder - FPS: {self.windowFPS}")

    def calculateDeltaTime(self):
        self.deltaTime = time.time() - self.begin
        self.begin = time.time()
        self.calculateAndShowFPS()
        
    def calculateAndShowFPS(self):
        self.totalTimePerSec += self.deltaTime
        if self.totalTimePerSec >= 1.0:
            self.showFPS()
            self.totalTimePerSec = 0
            self.windowFPS = 0
        else:
            self.windowFPS += 1
        
    def Loop(self):
        self.deltaTime = 0.0
        self.begin = 0.0
        
        while self.running:
            self.calculateDeltaTime()
            
            self.sceneManager.PollInput()
            
            self.sceneManager.Render()
            
            # self.gui.mainloop()
            pygame.display.update()
            # self.clock.tick(FPS)
    
def checkDependencies() -> None:
    required = { "pygame", "pillow" }
    installed = { pkg.key for pkg in pkg_resources.working_set }
    missing = required - installed
    
    if missing:
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
    
def tkinter_thread_handler():
    gui = GUIControl()
    gui.mainloop()
    
def pathfinder_thread_handler():
    Pathfinder = Window()
    Pathfinder.Loop()

def thread_handler():
    try:
        pathfinderThread = threading.Thread(target=pathfinder_thread_handler)
        tkinterThread = threading.Thread(target=pathfinder_thread_handler)
        
        pathfinderThread.start()
        tkinterThread.start()
        
        pathfinderThread.join()
        tkinterThread.join()
    except threading.ThreadError:
        logging.exception("Threading Error")


if __name__ == "__main__":
    # checkDependencies()
    
    # thread_handler()
    window = Window()
    window.Loop()
