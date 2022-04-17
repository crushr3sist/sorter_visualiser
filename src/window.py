# pygame
import pygame
from src.line_graph import Graph

# game class
class Window(Graph):
    # initialise the game
    def __init__(self, width: int, height: int, Array: list) -> None:
        # define screen size
        self.width = width
        self.height = height
        # run the initialise function
        self.screen = self.init_window()
        # create a sorter object
        super().__init__(width, height, Array)

    # initaliser function
    def init_window(self) -> pygame.Surface:
        # initialise pygame
        pygame.init()
        # set the window size
        size = (self.width, self.height)
        # set the window title
        pygame.display.set_caption(" Sorting Visualiser ")
        # set the window icon
        icon = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)
        # set the window size
        screen = pygame.display.set_mode(size)
        # return the screen
        return screen


# main function
if __name__ == "__main__":
    # create a game object
    window = Window(800, 600, [1, 2, 3])
    print(window)
