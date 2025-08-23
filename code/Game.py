from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu

import pygame

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        pygame.mixer_music.load('./assets/sounds/Dogs.mp3')
        pygame.mixer_music.play(-1)
        while True:
            menu = Menu(self.window)
            menu.run()
            pass
