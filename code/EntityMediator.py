import pygame

from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.Entity import Entity
from code.Player import Player
from code.PlayerShoot import PlayerShoot


class EntityMediator:

    @staticmethod
    def apply_damage(ent: Entity, damage: int):
        ent.health -= damage

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy): # Verify if is a Enemy entity
            if ent.rect.right < 0:
                ent.health = 0

        if isinstance(ent, PlayerShoot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def __verify_collision_between_entities(ent1, ent2):
        if isinstance(ent1, Enemy) and isinstance(ent2, PlayerShoot):
            if pygame.Rect.colliderect(ent1.rect, ent2.rect):
                EntityMediator.apply_damage(ent1, ent2.damage)
        if isinstance(ent1, PlayerShoot) and isinstance(ent2, Enemy):
            if pygame.Rect.colliderect(ent1.rect, ent2.rect):
                EntityMediator.apply_damage(ent2, ent1.damage)
        if (isinstance(ent1, Enemy) and isinstance(ent2, Player)) or (isinstance(ent1, Player) and isinstance(ent2, Enemy)):
            if pygame.Rect.colliderect(ent1.rect, ent2.rect):
                EntityMediator.apply_damage(ent1, ent2.damage)
                EntityMediator.apply_damage(ent2, ent1.damage)


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            ent = entity_list[i]
            EntityMediator.__verify_collision_window(ent)
            for j in range(i+1, len(entity_list)): # i + 1 prevent duplicated verification
                ent_to_compare = entity_list[j]
                if ent != ent_to_compare:
                    EntityMediator.__verify_collision_between_entities(ent, ent_to_compare)


    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)
