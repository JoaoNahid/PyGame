import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_TEXT_ORAGNE, COLOR_TEXT_WHITE


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/images/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

        self.menu_options = ('Start Game', 'Score', 'Exit' )

    def run(self):
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Quartástico", COLOR_TEXT_ORAGNE, ((WIN_WIDTH / 2), 100))
            self.menu_text(50, "Fanteto", COLOR_TEXT_ORAGNE, ((WIN_WIDTH / 2), 130))

            # Iterator for y position to write the options
            pos_y = 200
            for option in self.menu_options:
                self.menu_text(35, option, COLOR_TEXT_WHITE, ((WIN_WIDTH / 2), pos_y))
                pos_y = pos_y + 25

            pygame.display.flip()

            # Check all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Montserrat Medium", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)