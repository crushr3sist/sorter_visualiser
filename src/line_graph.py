import pygame, random
from sort import Sorter

class Graph(Sorter):
    # 
    def __init__(self, Array: list) -> None:
        super().__init__(Array)
        self.Array = Array
        self.screen = self.init_window()
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.font = pygame.font.SysFont("monospace", 15)
        self.text = self.font.render("", 1, (255,255,255))




# main function
if __name__ == "__main__":
    # create a game object
    window = Graph([random.randint(0,100) for i in range(100)])
    print(window)
