import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_TEXT_ORANGE, COLOR_TEXT_WHITE, COLOR_TEXT_ORANGE_700


class Menu:

    def __init__(self, window):
        self.window = window
        self.selected_option = 0
        self.surf = pygame.image.load('./assets/images/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

        self.menu_options = ('New Game 1P', 'New Game 2P - Competitive', 'Score', 'Exit' )

    def run(self) -> str:
        while True:
            # Draw Elements
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(70, "Quartástico", COLOR_TEXT_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(70, "Fanteto", COLOR_TEXT_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(self.menu_options)):
                if i == self.selected_option:
                    self.menu_text(35, self.menu_options[i], COLOR_TEXT_ORANGE_700, ((WIN_WIDTH / 2), 200 + (25 * i)))
                else:
                    self.menu_text(35, self.menu_options[i], COLOR_TEXT_WHITE, ((WIN_WIDTH / 2), 200 + (25 * i)))

            pygame.display.flip()

            # Check all events
            for event in pygame.event.get():
                # Close window
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close window
                    quit()  # End pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        self.selected_option += 1
                        if self.selected_option == len(self.menu_options):
                            self.selected_option = 0

                    if event.key == pygame.K_UP:
                        self.selected_option -= 1
                        if self.selected_option < 0:
                            self.selected_option = len(self.menu_options) - 1

                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        return self.menu_options[self.selected_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Montserrat Medium", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)