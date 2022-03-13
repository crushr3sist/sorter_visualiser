import pygame, random, time
from src.sort import Sorter


class Graph(Sorter):
    #
    def __init__(self, width: int, height: int, Array: list) -> None:
        # super init Sorter and Window class
        super().__init__(Array)
        # define screen size
        self.width = width
        self.height = height
        # run the initialise function
        self.screen = self.init_window()
        # set the background colour
        self.bg_colour = (0, 0, 0)
        self.column_color = (200, 0, 200)
        print("this code is reached")

    def create_columns(self, Array: list) -> list:
        # create a list of columns
        columns = []

        # looping the width
        for x in range(self.width):
            # create a column
            print(f"array variable{Array[x]}")
            column = pygame.Rect(x, Array[x], 1, self.height)
            # add the column to the list
            columns.append(column)
        # return the list

        return columns

    def draw_columns(self, columns: list) -> None:
        # looping the columns
        print(f"column variable {columns}")

        for column in tuple(columns):
            # draw the column
            pygame.draw.rect(self.screen, self.column_color, column)
