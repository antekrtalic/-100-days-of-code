import sys

import pygame

from wooden_boy import Wooden_Boy

class Window:


    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Pygame Window")

        self.boy = Wooden_Boy(self)

        self.bg_color = (0, 0, 255)


    def run_window(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            self.boy.blitme()

            pygame.display.flip()


if __name__ == "__main__":
    win = Window()
    win.run_window()
