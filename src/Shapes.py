import pygame

class Box(pygame.Rect):
    def __init__(self, *args) -> None:
        super().__init__(*args)

        # colors.
        self.BORDER_COLOR = (0, 0, 0)
        self.current_color = (255, 255, 255)

    def CheckClick(self, clicked: bool, color: tuple) -> tuple:
        if self.collidepoint(pygame.mouse.get_pos()) and clicked:
            print(f"x: {self.x/self.width}, y: {self.y/self.height}")
            self.current_color = color
            return (True, "Start")
        return (False, "None")
