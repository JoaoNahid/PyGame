import pygame.key

from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, ENTITY_DELAY
from code.Entity import Entity
from code.PlayerShoot import PlayerShoot


class Player(Entity):

    def __init__(self, name: str, position: tuple = (0,0), speed: int = 1, keyboard: int = 1):
        super().__init__(name, position, speed)
        self.keyboard = keyboard
        self.shoot_delay = ENTITY_DELAY['shoot']

    def update(self, ):
        pass

    def move(self, two_players: bool = False):
        pressed_key = pygame.key.get_pressed()
        # Move Y
        key_up = pygame.K_w if self.keyboard == 1 else pygame.K_UP
        key_down = pygame.K_s if self.keyboard == 1 else pygame.K_DOWN
        if pressed_key[key_up] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[key_down] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        # Move X
        key_left = pygame.K_a if self.keyboard == 1 else pygame.K_LEFT
        key_right = pygame.K_d if self.keyboard == 1 else pygame.K_RIGHT
        if pressed_key[key_left] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[key_right] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        # Shot
    def shoot(self):
        self.shoot_delay -= 1
        if self.shoot_delay == 0:
            self.reset_shoot_delay()
            pressed_key = pygame.key.get_pressed()
            key_shot = pygame.K_SPACE if self.keyboard == 1 else pygame.K_RCTRL
            if pressed_key[key_shot]:
                return PlayerShoot(name=f'{self.name}Shoot', position=(self.rect.centerx, self.rect.centery), speed=10)
        return None

    def reset_shoot_delay(self):
        self.shoot_delay = ENTITY_DELAY['shoot']