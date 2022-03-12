import pygame, random
from sort import Sorter
from window import Window
class Graph(Sorter, Window):
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
        self.bg_colour = (0,0,0)
        # set the line colour
        self.line_colour = (255,255,255)
        # set the font colour
        self.font_colour = (255,255,255)
        # set the font size
        self.font_size = 15
        # set the line width
        self.line_width = 1
        # set the gap between lines
        self.gap = 10
        # set the x and y axis
        self.x_axis = self.width//2
        self.y_axis = self.height//2
        # set the x and y axis length
        self.x_axis_length = self.width//2
        self.y_axis_length = self.height//2
        # set the x and y axis label
        self.x_axis_label = "X"
        self.y_axis_label = "Y"
        # set the x and y axis label size
        self.x_axis_label_size = self.font_size
        self.y_axis_label_size = self.font_size
        # set the x and y axis label x and y
        self.x_axis_label_x = self.x_axis - self.x_axis_length//2
        self.x_axis_label_y = self.y_axis + self.gap + self.x_axis_label_size
        self.y_axis_label_x = self.x_axis - self.gap - self.y_axis_label_size
        self.y_axis_label_y = self.y_axis - self.y_axis_length//2
        # set the x and y axis label font
        self.x_axis_label_font = pygame.font.SysFont('arial', self.x_axis_label_size)
        self.y_axis_label_font = pygame.font.SysFont('arial', self.y_axis_label_size)
        # set the x and y axis label text
        self.x_axis_label_text = self.x_axis_label_font.render(self.x_axis_label, True, self.font_colour)
        self.y_axis_label_text = self.y_axis_label_font.render(self.y_axis_label, True, self.font_colour)
        # set the x and y axis label text rect
        self.x_axis_label_text_rect = self.x_axis_label_text.get_rect()
        self.y_axis_label_text_rect = self.y_axis_label_text.get_rect()
        # set the x and y axis label text x and y
        self.x_axis_label_text_rect.x = self.x_axis_label_x
        self.x_axis_label_text_rect.y = self.x_axis_label_y
        self.y_axis_label_text_rect.x = self.y_axis_label_x
        self.y_axis_label_text_rect.y = self.y_axis_label_y
        # set the x and y axis label text x and y
        self.x_axis_label_text_rect.centerx = self.x_axis_label_x
        self.x_axis_label_text_rect.centery = self.x_axis_label_y
        self.y_axis_label_text_rect.centerx = self.y_axis_label_x
        self.y_axis_label_text_rect.centery = self.y_axis_label_y
        # set the x and y axis label font
        self.x_axis_label_font = pygame.font.SysFont('arial', self.x_axis_label_size)
        self.y_axis_label_font = pygame.font.SysFont('arial', self.y_axis_label_size)
        # set the x and y axis

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
