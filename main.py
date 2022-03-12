import random, pygame
from src.sort import Sorter
from src.window import Window


# application frontend class
class Application(Window):
    # initialise the application
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)
        # define screen size
        self.width  = width
        self.height = height
        # create a sorter object
        self.sorter = Sorter(self.get_random_array(100))
        # create a window object
        self.window = Window(self.width, self.height)
        # create a clock object
        self.clock = pygame.time.Clock()
        # create a font object
        self.font = pygame.font.SysFont("monospace", 15)
        # create a text object
        self.text = self.font.render("", 1, (255,255,255))
        # create a text position object
        self.text_pos = (0,0)
        # create a text position object
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.text_pos
        self.text_rect.top = self.text_pos[1]
        self.text_rect.left = self.text_pos[0]
        self.text_rect.bottom = self.text_pos[1]
        self.text_rect.right = self.text_pos[0]
        self.text_rect.topleft = self.text_pos
        self.text_rect.topright = self.text_pos
        self.text_rect.bottomleft = self.text_pos
        self.text_rect.bottomright = self.text_pos
        self.text_rect.midtop = self.text_pos
        self.text_rect.midleft = self.text_pos
        self.text_rect.midbottom = self.text_pos
        self.text_rect.midright = self.text_pos
        self.text_rect.center = self.text_pos
        self.text_rect.centerx = self.text_pos
        self.text_rect.centery = self.text_pos

    # main loop
    def run(self) -> None:
        # run the main loop
        while True:
            # get the time
            self.clock.tick(60)
            # get the events
            self.events()
            # update the game
            self.update()
            # draw the game
            self.draw()
    # get the events
    def events(self) -> None:
        # get the events
        for event in pygame.event.get():
            # check if the event is the quit event
            if event.type == pygame.QUIT:
                # quit the application
                pygame.quit()
                # exit the application
                exit()
            # check if the event is a key down event
            if event.type == pygame.KEYDOWN:
                # check if the key is the escape key
                if event.key == pygame.K_ESCAPE:
                    # quit the application
                    pygame.quit()
                    # exit the application
                    exit()
                # check if the key is the space key
                if event.key == pygame.K_SPACE:
                    # reset the application
                    self.reset()
    # update the game
    def update(self) -> None:
        # update the sorter
        self.sorter.update()
    # draw the game
    def draw(self) -> None:
        # clear the screen
        self.window.clear()
        # draw the sorter
        self.sorter.draw(self.window)
        # draw the text
        self.window.draw_text(self.text, self.text_rect)
        # update the display
        self.window.update()
    # reset the application
    def reset(self) -> None:
        # reset the sorter
        self.sorter.reset()
        # reset the text
        self.text = self.font.render("", 1, (255,255,255))
        # reset the text position
        self.text_pos = (0,0)
        # reset the text rectangle

    def get_random_array(self, size: int) -> list:
        return [random.randint(0,100) for i in range(size)]

# main function
if __name__ == "__main__":
    # create a game object
    app = Application(800,600)
    # run the main loop
    app.run()  

