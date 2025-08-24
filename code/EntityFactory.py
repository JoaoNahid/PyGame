from code.Background import Background
from code.Const import WIN_WIDTH, ENTITY_SPEED


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