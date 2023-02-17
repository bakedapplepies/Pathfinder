import sys
import pygame
# from pygame.locals import *

from Shapes import Box
from Text import Text

# types of boxes
# global START_POINT
# global END_POINT
# global WALL
# global BOX_NONE
# global box_type
START_POINT = (229, 41, 48)
END_POINT = (47, 41, 212)
WALL = (30, 30, 30)
BOX_NONE = (255, 255, 255)

# default colors
BACKGROUND_COLOR = (255, 255, 255)

# default values
RESOLUTION = (900, 800)  # x, y
SQUARE_SIZE = 20

# fps clock
fpsClock = pygame.time.Clock()
FPS = 60

# initialize pygame
pygame.init()


class Pathfinder:
    def __init__(self) -> None:
        # main window
        pygame.display.set_caption("Pathfinder")
        # pygame
        self.gameWindow = pygame.display.set_mode(RESOLUTION)

        # variables
        self.box_type = BOX_NONE
        self.start_point = None

        # grid
        self.grid = []
        for x in range(0, 800, SQUARE_SIZE):
            for y in range(0, 800, SQUARE_SIZE):
                self.grid.append(Box(x, y, SQUARE_SIZE, SQUARE_SIZE))

        # text
        self.modeFont = Text(None, 24)
        self.modeFontSurface = self.modeFont.render("Mode: q", True, self.modeFont.DEFAULT_COLOR, None)

    def GetInput(self) -> None:
        boxClicked: bool = False
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                boxClicked = True
            if event.type == pygame.KEYDOWN and keys[pygame.K_1]:
                print("Start node")
                
                self.box_type = START_POINT
            
        self.BoxClick(boxClicked, self.box_type)

    def BoxClick(self, clicked: bool, color: tuple) -> None:
        for box in self.grid:
            if box == self.start_point:
                result = box.CheckClick(clicked, self.box_type)
                if result[0]:
                    if result[1] == "Start":
                        self.start_point = box
            else:
                box.CheckClick(clicked, BOX_NONE)

    def Render(self) -> None:
        # drawing order MATTERS
        self.gameWindow.fill(BACKGROUND_COLOR)
        self.gameWindow.blit(self.modeFontSurface, (800, 0))
        for box in self.grid:
            pygame.draw.rect(self.gameWindow, box.current_color, box)
            pygame.draw.rect(self.gameWindow, box.BORDER_COLOR, box, 1)
        
    def main(self) -> None:
        run: bool = True;

        while run:

            self.GetInput()

            self.Render()

            pygame.display.update()
            fpsClock.tick(FPS)
            # print(fpsClock.get_fps())


if __name__ == "__main__":
    program = Pathfinder()
    program.main()
