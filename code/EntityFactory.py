import random

from code.Background import Background
from code.Const import WIN_WIDTH, ENTITY_SPEED, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0), ENTITY_SPEED[f'Level1Bg{i}']))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH,0), ENTITY_SPEED[f'Level1Bg{i}']))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2), 1)
            case 'Player2':
                return Player('Player2', (10, WIN_HEIGHT * 0.75), 1, keyboard=2)
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT - 30)))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(0, WIN_HEIGHT - 30)))