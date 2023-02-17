import sys
import pygame
import time

from Grid import Grid


RESOLUTION = (1200, 800)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 60

pygame.init()

class Window:
    def __init__(self):
        # Main window
        pygame.display.set_caption("Pathfinder")
        self.window = pygame.display.set_mode(RESOLUTION)
        
        # Game variables
        self.running = True
        
        # Player
        # self.player = pygame.Rect(0, 0, 100, 100)
        
        # Grid
        self.grid = Grid()
        
    def Loop(self):
        deltaTime = 0
        begin = time.time()
        while self.running:
            deltaTime = time.time() - begin
            begin = time.time()
            
            self.PollInput()
            
            self.Render()
            
            pygame.display.update()
            clock.tick(FPS)
            
    def PollInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    def Render(self):
        self.window.fill(WHITE)
        self.DrawGrid()
        
    def DrawGrid(self):
        pass
    

if __name__ == "__main__":
    Pathfinder = Window()
    Pathfinder.Loop()
    