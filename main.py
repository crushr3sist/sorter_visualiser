import random, pygame, time
from src.window import Window

# TODO - update the readme to confirm animation is working !!!
# application frontend class
class Application(Window):
    # initialise the application
    def __init__(self, width: int, height: int) -> None:
        # define screen size
        self.width = width

        self.height = height
        self.array_to_sort = self.get_random_array(self.height, self.width)

        super().__init__(self.width, self.height, self.array_to_sort)
        # create a window object
        # create a clock object
        self.clock = pygame.time.Clock()
        # create a font object
        self.font = pygame.font.SysFont("monospace", 15)
        # create a text object
        self.text = self.font.render("", 1, (255, 255, 255))

    # main loop
    def run(self) -> None:
        # run the main loop
        while True:
            # get the time
            self.clock.tick(60)
            # get the events
            self.events()

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
                    self.sort_the_array()
                if event.key == pygame.K_s:
                    self.animate()

                if event.key == pygame.K_r:
                    self.reset()

    # update the game
    def update(self) -> None:
        pygame.event.pump()
        pygame.display.flip()
        self.screen.fill((0, 0, 0))

    def animate(self) -> None:
        # set the tick rate to a lower value
        self.clock.tick(1)
        # make a generator for the bubble sort
        for i in self.bubble_sort():
            # reassign the array to the generator yield
            self.array_to_sort = i
            self.draw_columns(self.create_columns(self.array_to_sort))
            self.update()

    # reset the application
    def reset(self) -> None:

        self.initial_state()
        self.update()

    def initial_state(self) -> None:
        self.screen.fill(self.bg_colour)
        self.array_to_sort = self.get_random_array(self.height, self.width)

        self.draw_columns(self.create_columns(self.array_to_sort))

    def get_random_array(self, height, width) -> list:
        return [random.randint(0, height) for i in range(0, width)]


# main function
if __name__ == "__main__":
    # create a game object
    app = Application(800, 600)
    # run the main loop
    app.run()