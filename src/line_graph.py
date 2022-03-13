import pygame, random, time
from src.sort import Sorter

class Graph(Sorter):
    # 
    def __init__(self, Array: list) -> None:
        # super init Sorter and Window class
        super().__init__(Array)
        # define screen size
        self.width  = 800
        self.height = 600
        # run the initialise function
        self.screen = self.init_window()
        # set the background colour
        self.bg_colour = (255,255,0)
        print('this code is reached')

    def load_columns(self) -> None:
        
        ...