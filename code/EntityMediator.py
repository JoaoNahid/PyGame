from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.PlayerShoot import PlayerShoot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy): # Verify if is a Enemy entity
            if ent.rect.right < 0:
                ent.health = 0

        if isinstance(ent, PlayerShoot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            ent = entity_list[i]
            EntityMediator.__verify_collision_window(ent)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)