import pygame

class Text(pygame.font.Font):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        
        # colors
        self.DEFAULT_COLOR = (0, 0, 0)
